from ..utils.command import Command
from ..utils.tokenizer import Tokenizer
from ..utils.filter import Filter
from ..utils.ngram import NGram
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from collections import Counter
import time
import logging

# Configure logging to write to a file
logging.basicConfig(
    filename="data/predictor_logs.txt",  # file where logs will go
    filemode="w",                   # overwrite each time
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

class TrainNaiveBayes(Command):
    def __init__(self, data: list, ngrams=[1,2], include_stopwords = False):
        self.__data = data
        self.__ngrams = ngrams
        self.__stopwords = include_stopwords
        self.__vocab_size = set()
        self.__class_counter = {}
        self.__class_word_counter = {}
        self.__unigrams = Counter()
        self.__bigrams = Counter()
        self.__trigrams = Counter()

    def execute(self):
        #self.__vocab_size.update(["POSITIVE", "NEGATIVE", "NEUTRAL"])
        for content, label in self.__data:
            tokens = Tokenizer(content).execute()

            if self.__stopwords:            
                tokens = Filter(tokens).execute()

            all_ngrams = {}
            unigrams = NGram(tokens, n=1).execute()
            bigrams = NGram(tokens, n=2).execute()
            trigrams = NGram(tokens, n=3).execute()

            self.__unigrams.update(unigrams)
            self.__bigrams.update(bigrams)
            self.__trigrams.update(trigrams)
            all_ngrams.update(unigrams)
            all_ngrams.update(bigrams)
            all_ngrams.update(trigrams)

            for gram in all_ngrams:
                self.__vocab_size.add(gram)

            if label not in self.__class_counter:
                self.__class_counter[label] = 0
                self.__class_word_counter[label] = {}
            
            self.__class_counter[label] += 1

            for ngram, count in all_ngrams.items():
                self.__class_word_counter[label][ngram] = (self.__class_word_counter[label].get(ngram, 0) + count)
                
        return {
            "class_count": self.__class_counter, 
            "class_word_count": self.__class_word_counter, 
            "vocab_size": len(self.__vocab_size),
            "unigrams": self.__unigrams,
            "bigrams": self.__bigrams,
            "trigrams": self.__trigrams
            }