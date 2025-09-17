import math
from ..utils.command import Command
from ..utils.tokenizer import Tokenizer
from ..utils.filter import Filter
from ..utils.ngram import NGram

class Predictor(Command):
    def __init__(self, text: str, class_count: dict, class_word_count: dict, vocab_size: int, ngrams=[1,2,3]) -> None:
        self.__text = text
        self.__class_count = class_count
        self.__class_word_count = class_word_count
        self.__vocab_size = vocab_size
        self.__ngrams = ngrams
    
    def execute(self):
        tokens = Filter(Tokenizer(self.__text, False).execute()).execute()
        total_documents = sum(self.__class_count.values())
        scores = {}

        all_ngrams = {}
        for ngram in self.__ngrams:
            ngrams = NGram(tokens, n=ngram).execute()
            for gram, count in ngrams.items():
                all_ngrams[gram] = all_ngrams.get(gram, 0) + count

        for label in self.__class_word_count.keys():
            probability = math.log(self.__class_count[label] / total_documents)
            for ngram, count in all_ngrams.items():
                token_count = self.__class_word_count[label].get(ngram, 0)
                total_tokens = sum(self.__class_word_count[label].values())

                likelihood = math.log((token_count + 1) / (total_tokens + self.__vocab_size))
                probability += count * likelihood
            
            scores[label] = probability
            
        return max(scores, key=scores.get)
