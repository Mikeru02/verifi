import random
from .command import Command
from .file_handler import Open_File

class Tupler(Command):
    def __init__(self, csv_file_path: str, type: str = "content") -> None:
        self.__csv_data = Open_File(csv_file_path).execute()
        self.__data = []
        self.__type = type
    
    def execute(self):
        if self.__type == "content":
            for data in self.__csv_data:
                content = data["content"]
                label = data["label"]
                created_tuple = (content, label)
                self.__data.append(created_tuple)

            random.shuffle(self.__data)

            return self.__data
        elif self.__type == "title":
            for data in self.__csv_data:
                title = data["title"]
                label = data["label"]
                created_tuple = (title, label)
                self.__data.append(created_tuple)

            random.shuffle(self.__data)

            return self.__data
        else:
            raise ValueError(f"Invalid type {self.__type}")
    