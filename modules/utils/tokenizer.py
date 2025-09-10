import re
from .command import Command
from .tagger import Tagger

class Tokenizer(Command):
    def __init__(self, text: str, special_characters = True) -> None:
        self.__text = text
        self.__special_characters = special_characters
        self.__tokens = []

    
    def execute(self) -> list:
        # Step 1: Split into sentences
        sentences = re.split(r'(?<=[.!?])\s+', self.__text)

        for sentence in sentences:
            if not sentence.strip():
                continue

            words = sentence.strip().split()
            words = Tagger(words).execute()

            if self.__special_characters:
                self.__tokens.append("<s>")
            
            for word in words:
                self.__tokens.append(word)
            
            if self.__special_characters:
                self.__tokens.append("</s>")

        return self.__tokens