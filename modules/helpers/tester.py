import time
import sys
import threading
from data.statistics import Statistics
from ..utils.command import Command
from ..core.predictor import Predictor

class Tester(Command):
    def __init__(self, model: dict, test_data: list, include_statistics =  False, number_of_items = 10) -> None:
        self.__model = model
        self.__class_count = model['class_count']
        self.__class_word_count = model['class_word_count']
        self.__vocab_size = model['vocab_size']
        self.__test_data = test_data
        self.__number_of_items = number_of_items
        self.__include_statistics = include_statistics
        self.__score = 0
    
    def statistics_checker(self, start_time, stop_flag):
        while not stop_flag["stop"]:
            elapse = int(time.time() - start_time)
            sys.stdout.write(f"\rRuntime: {elapse} seconds | Document Count: {Statistics.get_document_count()} | Recent doc kb: {Statistics.get_recent_kb():.4f} kb | Recent time: {Statistics.get_recent_time():.4f} s")
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\n")

    def execute(self) -> int:
        if self.__include_statistics:
            start_time = time.time()
            stop_flag = {"stop": False}

            ticker_thread = threading.Thread(target=self.statistics_checker, args=(start_time, stop_flag))
            ticker_thread.daemon = True
            ticker_thread.start()

            total_size = Statistics.get_total_size()
            count = Statistics.get_document_count()

            for document in self.__test_data[:self.__number_of_items]:
                content, label = document

                size_kb = len(content.encode("utf-8")) / 1024
                total_size += size_kb
                count += 1

                predict_start_time = time.time()
                prediction = Predictor(content, model=self.__model).execute()
                elapsed_prediction = time.time() - predict_start_time
                Statistics.add_document(size_kb, elapsed_prediction)

                if prediction == label:
                    self.__score += 1

            stop_flag["stop"] = True
            accuracy = self.__score / self.__number_of_items
            Statistics.compute_average()
            print(f"\n\nPrediction Score: {self.__score}")
            print(f"Accuracy: {accuracy:.2%}")
            print(f"Average kb: {Statistics.get_average_kb():.4f} kb | Average Process Time: {Statistics.get_average_time():.4f} s")

        return self.__score
