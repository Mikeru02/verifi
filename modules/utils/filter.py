from data.lists import stop_words
from .command import Command

class Filter(Command):
    def __init__(self, tokens: list) -> None:
        self.__tokens = tokens
        self.__filtered_tokens = []

    def execute(self) -> list:
        for token in self.__tokens:
            if token.lower() not in stop_words:
                self.__filtered_tokens.append(token)
        
        return self.__filtered_tokens