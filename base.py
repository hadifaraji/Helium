from helium import *
from selenium.webdriver import ChromeOptions
from config import Config
class Base:
    def __init__(self):
        self.url = Config().root()
        options = ChromeOptions()
        options.add_argument("--disable-notifications")
        start_chrome(self.url, options=options,maximize=True)