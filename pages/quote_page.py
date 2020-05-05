
"""
    Will be getting the whole page as an object from the app.py

"""

from locators.quote_page_locator import QuotePageLocater
from parsers.quote import QuoteParser

class QuotePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self):
        #  created an object of a quote from a complete page and passed into    
        return [
            QuoteParser(e)
            for e in self.browser.find_elements_by_css_selector(
                QuotePageLocater.QUOTE
                )
        ]



