from bs4 import BeautifulSoup
from ..utils.command import Command

class PolitifactParser(Command):
    def __init__(self, soup: BeautifulSoup) -> None:
        self.__soup = soup

    def execute(self):
        title = self.__soup.find('div', class_="m-statement__quote")
        return title