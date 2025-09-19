import requests
import random
import time
import cloudscraper
from newspaper import Article
from bs4 import BeautifulSoup
from ..utils.command import Command
from ..utils.normalizer import Normalizer
from data.lists import headers

class Scraper(Command):
    def __init__(self, url: str) -> None:
        self.__url = url
    
    def get_headers(self) -> dict:
        return random.choice(headers)
    
    def execute(self):
        sleep_time = random.uniform(6, 10)
        #time.sleep(sleep_time)

        response = requests.get(self.__url, headers=self.get_headers(), timeout=15)
        response.raise_for_status()

        article = Article(self.__url)
        article.set_html(response.text)
        article.parse()

        return article.title, article.text, article.authors

class ScraperV2(Command):
    def __init__(self, url) -> None:
        self.__url = url

    def execute(self):
        try:
            header = random.choice(headers)
            sleep_time = random.uniform(2, 6)
            print("Sleep Time: ", sleep_time)
            time.sleep(sleep_time)

            response = requests.get(self.__url, headers=header, timeout=15)
            response.raise_for_status()

            print("Response: ", response)

            article = Article(self.__url)
            article.set_html(response.text)
            article.parse()


            normalized_article = Normalizer(article.text).execute()
            return normalized_article
        except Exception as error:
            print(f"Failed {self.__url} -> {error}")

class ScraperV3(Command):
    def __init__(self, url: str) -> None:
        self.__url = url
    
    def execute(self):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://www.google.com/",
            "Accept-Language": "en-US,en;q=0.9"
        }
        scraper = cloudscraper.create_scraper(
            browser={"browser": "chrome", "platform": "windows", "mobile": False}
        )
        response = scraper.get(self.__url, headers=header, timeout=20)

        if response.status_code == 200:
            article = Article("")
            article.set_html(response.text)
            article.parse()
            return Normalizer(article.text).execute(), article.title
        else:
            print("Failed with status:", response.status_code)
