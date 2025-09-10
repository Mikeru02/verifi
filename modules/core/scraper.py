import requests
import random
from bs4 import BeautifulSoup
from ..utils.command import Command
from data.lists import headers

class Scraper(Command):
    def __init__(self, url: str) -> None:
        self.__url = url
    
    def get_headers(self) -> dict:
        return random.choice(headers)
    
    def execute(self):
        response = requests.get(self.__url, headers=self.get_headers())
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        else:
            print(f"Failed to retrieve data from URL: code_{response.status_code}")
            return None
