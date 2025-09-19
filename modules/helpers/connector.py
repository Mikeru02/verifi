from pathlib import Path
from data.input_data import data
from data.lists import domain_source
from ..core.scraper import Scraper, ScraperV3
from ..core.predictor import Predictor
from models.models import NaiveBayes, TuplesConverter
from ..utils.file_handler import Save_File, Open_File
from ..utils.normalizer import Normalizer
from ..utils.command import Command
import math
import re

class Connector(Command):
    def __init__(self, title: str, content: str, url:str = None) -> None:
        self.__url = url
        self.__title = title
        self.__content = content
        self.__title_tuples_path = "models/grams_last_tittle_tupple_ngrams.pkl"
        self.__content_tuples_path = "models/grams_last_tupple_ngrams.pkl"
        self.__title_model_path = "models/grams_last_titles.pkl"
        self.__content_model_path = "models/grams_last_ngrams.pkl"
        self.__csv_file_path = "data/final_data.csv"
        self.__article_list = []
        self.__scraped_urls = set()
    
    def scrape_data(self):
        if Path(self.__csv_file_path).exists():
            scraped_data = Open_File(self.__csv_file_path).execute()
            for row in scraped_data:
                if "url" in row and row["url"]:
                    self.__scraped_urls.add(row["url"])
            self.__article_list.extend(scraped_data)
        
        for news_link, label in data:
            if news_link in self.__scraped_urls:
                continue
            try:
                scraper = Scraper(news_link)
                title, content, authors = scraper.execute()

                normalized_article = Normalizer(content).execute()
                if authors:
                    authors = ", ".join(authors)
                else:
                    authors = ""
                
                self.__article_list.append({
                    "url": news_link,
                    "title": title,
                    "content": normalized_article,
                    "authors": authors,
                    "label": label
                })
            except Exception as error:
                print(f"Failed {news_link} -> {error}")

        Save_File(self.__csv_file_path, self.__article_list).execute()

    def train_and_get_model(self):
        title_tuples = TuplesConverter(self.__title_tuples_path, self.__csv_file_path, "title").execute()
        content_tuples = TuplesConverter(self.__content_tuples_path, self.__csv_file_path, "content").execute()
        
        title_percentage = math.ceil(len(title_tuples) * 0.2)
        content_percentage = math.ceil(len(content_tuples) * 0.2)

        title_test_tuples = title_tuples[:title_percentage]
        title_train_tuples = title_tuples[:title_percentage:]

        content_test_tuples = content_tuples[:content_percentage]
        content_train_tuples = content_tuples[content_percentage:]

        self.title_model = NaiveBayes(self.__title_model_path, title_train_tuples).execute()
        self.content_model = NaiveBayes(self.__content_model_path, content_train_tuples).execute()
    
    def compute_scores(self, title_scores, content_scores):
        final_scores = {
            "True": content_scores["True"] + title_scores["True"],
            "False": content_scores["False"] + title_scores["False"],
        }
        return final_scores
    
    def check_domain_source(self, scores):
        url_score = 0
        if self.__url is not None:
            for domain, points_dict in domain_source.items():
                if re.search(domain, self.__url, re.IGNORECASE):
                    print(f"Matched {domain} in {self.__url}, adding points {points_dict}")
                    for label, points in points_dict.items():
                        if label in scores:
                            scores[label] += points
                    
            return scores
    def execute(self):
        self.train_and_get_model()

        if self.__url is not None:
            article, title = ScraperV3(self.__url).execute()
        else:
            article, title = self.__content, self.__title
        
        title_result, title_scores = Predictor(title, self.title_model).execute()
        content_result, content_scores = Predictor(article, self.content_model).execute()

        
        final_scores = self.compute_scores(title_scores, content_scores)
        print("Scores before domain check: ", final_scores)
        final_scores = self.check_domain_source(final_scores)
        print(final_scores)
        
        print(max(final_scores, key=final_scores.get))
        return max(final_scores, key=final_scores.get), final_scores
        
