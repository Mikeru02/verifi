from ..utils.command import Command
from ..utils.tokenizer import Tokenizer
from ..utils.filter import Filter

class TrainNaiveBayes(Command):
    def __init__(self, data: list, include_stopwords = False):
        self.__data = data
        self.__stopwords = include_stopwords
        self.__vocab_size = set()
        self.__class_counter = {}
        self.__class_word_counter = {}

    def execute(self):
        for content, label in self.__data:
            tokens = Tokenizer(content).execute()

            if self.__stopwords:            
                tokens = Filter(tokens).execute()

            self.__vocab_size.update(tokens)

            if label not in self.__class_counter:
                self.__class_counter[label] = 0
                self.__class_word_counter[label] = {}
            
            self.__class_counter[label] += 1

            for token in tokens:
                self.__class_word_counter[label][token] = self.__class_word_counter[label].get(token, 0) + 1
            
        return self.__class_counter, self.__class_word_counter, len(self.__vocab_size)