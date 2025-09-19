from ..utils.command import Command
from PIL import Image
import pytesseract

class Converter(Command):
    def __init__(self, type: str, path: str) -> None:
        self.__type = type
        self.__path = path
    
    def execute(self):
        if self.__type == "image":
            image = Image(self.__path)
            text = pytesseract.image_to_string(image)
            return text
        