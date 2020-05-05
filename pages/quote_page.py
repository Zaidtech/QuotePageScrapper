from typing import List
from selenium.webdriver.support.ui import Select
"""
    Will be getting the whole page as an object from the app.py

"""

from locators.quote_page_locator import QuotePageLocater
from parsers.quote import QuoteParser

class QuotePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser] :
        #  created an object of a quote from a complete page and passed into    
        return [
            QuoteParser(e)
            for e in self.browser.find_elements_by_css_selector(
                QuotePageLocater.QUOTE
                )
        ]

    @property
    def author_dropdown(self) -> Select :
         element = self.browser.find_element_by_css_selector(
             QuotePageLocater.AUTHOR_DROPDOWN
         ) 
         return Select(element)

    def select_author(self, author_name:str):
        self.author_dropdown.select_by_visible_text(author_name)




