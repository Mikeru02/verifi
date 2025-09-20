import math
from ..utils.command import Command
from ..utils.tokenizer import Tokenizer
from ..utils.filter import Filter
from ..utils.ngram import NGram, Interpolate
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging

logging.basicConfig(
    filename="data/predictor_logs.txt",  # file where logs will go
    filemode="w",                   # overwrite each time
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
class Predictor(Command):
    def __init__(self, text: str, model: dict, ngrams=[1,2, 3]) -> None:
        self.__model = model
        self.__text = text
        self.__class_count = model["class_count"]
        self.__class_word_count = model["class_word_count"]
        self.__vocab_size = model["vocab_size"]
        self.__ngrams = ngrams
        self.__analyzer = SentimentIntensityAnalyzer()

    def execute(self):
        tokens = Filter(Tokenizer(self.__text, False).execute()).execute()

        all_ngrams = {}
        for ngram in self.__ngrams:
            ngrams = NGram(tokens, n=ngram).execute()
            for gram, count in ngrams.items():
                all_ngrams[gram] = all_ngrams.get(gram, 0) + count

        total_documents = sum(self.__class_count.values())
        scores = {}

        for label in self.__class_word_count.keys():
            probability = math.log(self.__class_count[label] / total_documents)
            for ngram, count in all_ngrams.items():
                if len(ngram) == 3:
                    w1, w2, w3 = ngram
                    interpolation_prob = Interpolate(w1, w2, w3, self.__model).execute()
                    likelihood = math.log(interpolation_prob + 1e-9)
                else:
                    token_count = self.__class_word_count[label].get(ngram, 0)
                    total_tokens = sum(self.__class_word_count[label].values())
                    likelihood = math.log((token_count + 1) / (total_tokens + self.__vocab_size))

                probability += count * likelihood
            scores[label] = probability

        # sentiment = self.__analyzer.polarity_scores(self.__text)
        # compound_score = sentiment["compound"]

        # if abs(compound_score) > 0.5:
        #     # Strong sentiment → slightly favor "False"
        #     scores["False"] += 20
        #     scores["True"] -= 20
        # else:
        #     # Neutral sentiment → slightly favor "True"
        #     scores["True"] += 20
        #     scores["False"] -= 20

        return max(scores, key=scores.get), scores
