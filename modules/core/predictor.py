import math
from ..utils.command import Command
from ..utils.tokenizer import Tokenizer
from ..utils.filter import Filter

class Predictor(Command):
    def __init__(self, text: str, class_count: dict, class_word_count: dict, vocab_size: int) -> None:
        self.__text = text
        self.__class_count = class_count
        self.__class_word_count = class_word_count
        self.__vocab_size = vocab_size
    
    def execute(self):
        tokens = Filter(Tokenizer(self.__text, False).execute()).execute()
        total_documents = sum(self.__class_count.values())
        scores = {}

        #print(tokens)

        for label in self.__class_word_count.keys():
            probability = math.log(self.__class_count[label] / total_documents)
            #print(f"--> logprior({label}): log({self.__class_count[label]} / {total_documents}) = {probability}")

            for token in tokens:
                token_count = self.__class_word_count[label].get(token, 0)
                total_tokens = sum(self.__class_word_count[label].values())

                likelihood = math.log((token_count + 1) / (total_tokens + self.__vocab_size))
                #print(f"---> {token}: log({token_count + 1} / {total_tokens + self.__vocab_size}) = {likelihood}")

                probability += likelihood

            #print(f"{label} at {probability}")

            scores[label] = probability

        return max(scores, key=scores.get)
