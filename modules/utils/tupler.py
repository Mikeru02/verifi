import random
from .command import Command
from .file_handler import Open_File

class Tupler(Command):
    def __init__(self, csv_file_path: str) -> None:
        self.__csv_data = Open_File(csv_file_path).execute()
        self.__data = []
    
    def execute(self):
        for data in self.__csv_data:
            content = data["text"]
            label = data["label"]
            created_tuple = (content, label)
            self.__data.append(created_tuple)

        random.shuffle(self.__data)

        return self.__data

    