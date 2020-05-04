
"""
    Will be getting the whole page as an object from the app.py

"""
from bs4 import BeautifulSoup
from locators.quote_page_locator import QuotePageLocater
from parsers.quote import QuoteParser

class QuotePage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        #  created an object of a quote from a complete page and passed into
        locator = QuotePageLocater.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]



