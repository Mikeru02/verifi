import csv
import json
import pickle
from pathlib import Path
from .command import Command

class Open_File(Command):
    def __init__(
            self, file_path: str, mode: str = "r", encoding: str = "utf-8"
        ) -> None:

        self.__path = Path(file_path)
        self.__file_extension = self.__path.suffix.lower()
        self.__mode = mode
        self.__encoding = encoding

    def execute(self):
        if self.__file_extension == ".txt":
            with open(self.__path, self.__mode, encoding=self.__encoding) as file:
                return file.read()
            
        elif self.__file_extension == ".csv":
            rows = []
            with open(self.__path, self.__mode, encoding=self.__encoding, newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    rows.append(row)
                return rows
            
        elif self.__file_extension == ".json":
            with open(self.__path, self.__mode, encoding=self.__encoding) as file:
                return json.load(file)
            
        elif self.__file_extension == ".pkl":
            with open(self.__path, self.__mode) as file:
                return pickle.load(file) 

        else:
            raise ValueError(f"Unsupported {self.__file_extension} file")

class Save_File(Command):
    def __init__(
            self, file_path: str, inputted_data, mode: str = "w", encoding: str = "utf-8"
        ) -> None:

        self.__path = Path(file_path)
        self.__file_extension = self.__path.suffix.lower()
        self.__inputted_data = inputted_data
        self.__mode = mode
        self.__encoding = encoding
    
    def execute(self):
        if not self.__inputted_data:
            raise ValueError(f"The inputted_data can not be empty!")
        
        if self.__file_extension == ".txt":
            with open(self.__path, self.__mode, encoding=self.__encoding) as file:
                file.write(self.__inputted_data)

            return True
        
        elif self.__file_extension == ".csv":
            is_existing = self.__path.exists()

            with open(self.__path, self.__mode, encoding=self.__encoding, newline="") as file:
                writer = csv.DictWriter(file, fieldnames=self.__inputted_data[0].keys())
                
                if not is_existing or self.__mode == "w":
                    writer.writeheader()
                
                writer.writerows(self.__inputted_data)

            return True
        
        elif self.__file_extension == ".json":
            with open(self.__path, self.__mode, encoding=self.__encoding) as file:
                json.dump(self.__inputted_data, file, indent=4)

            return True
        
        elif self.__file_extension == ".pkl":
            with open(self.__path, self.__mode) as file:
                pickle.dump(self.__inputted_data, file)
            
            return True

        else:
            raise ValueError(f"Unsupported {self.__file_extension} file")