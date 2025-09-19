from collections import Counter, defaultdict
from .command import Command

class NGram(Command):
    def __init__(self, tokens: list, n = 3) -> None:
        self.__tokens = tokens
        self.__n = n
        self.__ngrams = Counter()

    def execute(self):
        for i in range(len(self.__tokens)):
            if self.__n == 1:
                grams = self.__tokens[i]
            else:
                if i + self.__n <= len(self.__tokens):
                    grams = tuple(self.__tokens[i: i + self.__n])
                else: 
                    continue

            self.__ngrams[grams] += 1
        
        return self.__ngrams

class Interpolate(Command):
    def __init__(self, word1: str, word2: str, word3: str, model: dict, weights = (0.1, 0.3, 0.6)) -> None:
        self.__word1 = word1
        self.__word2 = word2
        self.__word3 = word3
        self.__weights = weights
        self.__model = model
        self.__unigrams = self.__model['unigrams']
        self.__bigrams = self.__model['bigrams']
        self.__trigrams = self.__model['trigrams']

    def execute(self):
        # P(w₃ | w₁, w₂) = λ₁ × P(w₃) + λ₂ × P(w₃ | w₂) + λ₃ × P(w₃ | w₁, w₂)

        # P(w₃)
        prob1 = self.__unigrams.get(self.__word3) / sum(self.__unigrams.values()) if self.__word3 in self.__unigrams else 0

        # P(w₃ | w₂)
        prob2 = self.__bigrams.get((self.__word2, self.__word3)) / self.__unigrams.get(self.__word2) if (self.__word2, self.__word3) in self.__bigrams else 0

        # P(w₃ | w₁, w₂)
        prob3 = self.__trigrams.get((self.__word1, self.__word2, self.__word3)) / self.__bigrams.get((self.__word1, self.__word2)) if (self.__word1, self.__word2, self.__word3) in self.__trigrams else 0

        return (prob1 * self.__weights[0]) + (prob2 * self.__weights[1]) + (prob3 * self.__weights[2])
