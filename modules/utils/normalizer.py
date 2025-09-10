import re
from .command import Command

class Normalizer(Command):
    def __init__(self, text: str) -> None:
        self.__text = text
    
    def execute(self) -> str:
        self.__text = self.__text.lower()
        self.__text = re.sub(r"\W", "", self.__text)
        self.__text = re.sub(r"\s+", "", self.__text)
        return self.__text