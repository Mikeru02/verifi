from pathlib import Path
from modules.utils.command import Command
from modules.utils.file_handler import Open_File, Save_File
from modules.utils.tupler import Tupler
from modules.core.trainer import TrainNaiveBayes

class TuplesConverter(Command):
    def __init__(self, model_file_path: str, csv_file_path: str) -> None:
        self.__model_file_path = Path(model_file_path)
        self.__csv_file_path = csv_file_path
    
    def execute(self) -> list:
        if self.__model_file_path.exists():
            model = Open_File(self.__model_file_path, mode="rb").execute()
            return model
        else:
            data = Tupler(self.__csv_file_path).execute()
            Save_File(self.__model_file_path, data, mode="wb").execute()
            return data
        
class NaiveBayes(Command):
    def __init__(self, model_file_path: str, document_data: list) -> None:
        self.__model_file_path = Path(model_file_path)
        self.__document_data = document_data

    def execute(self):
        if self.__model_file_path.exists():
            model = Open_File(self.__model_file_path, mode="rb").execute()
            return model
        else:
            class_count, class_word_count, vocab_size = TrainNaiveBayes(self.__document_data, include_stopwords=True).execute()

            model_data = {
                "class_count": class_count,
                "class_word_count": class_word_count,
                "vocab_size": vocab_size
            }

            Save_File(self.__model_file_path, model_data, mode="wb").execute()
            return model_data