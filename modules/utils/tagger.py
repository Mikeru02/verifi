import re
from data.lists import negative_words
from .command import Command
from .normalizer import Normalizer

class Tagger(Command):
    def __init__(self, tokens: list) -> None:
        self.__tokens = tokens
        self.__updated = []
        self.__negated = False
    
    def execute(self) -> list:
        for token in self.__tokens:
            normalized_token = Normalizer(token).execute()

            if token.lower() in negative_words:
                self.__negated = True
                self.__updated.append(normalized_token)
            elif re.search(f"[.!?,;:]", token):
                self.__updated.append(token)
                self.__negated = False
            else:
                self.__updated.append(f"NOT_{normalized_token}" if self.__negated else normalized_token)

        return self.__updated