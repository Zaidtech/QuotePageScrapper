from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select


from locators.quote_page_locator import QuotePageLocater
from parsers.quote import QuoteParser

class QuotePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
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

    @property
    def tags_dropdown(self) -> Select :
         element = self.browser.find_element_by_css_selector(
             QuotePageLocater.TAG_DROPDOWN
         ) 
         return Select(element)

    @property 
    def search_button(self):
        return self.browser.find_element_by_css_selector(
            QuotePageLocater.SEARCH_BUTTON
        
        )

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tags_dropdown.options]

    def select_tag(self, tag_name:str):
        self.tags_dropdown.select_by_visible_text(tag_name)
    
    def select_author(self, author_name:str):
        self.author_dropdown.select_by_visible_text(author_name)

    
    def search_for_quotes(self, author_name:str, tag_name:str) -> List[QuoteParser]:
        self.select_author(author_name)
        try:
            self.select_tag(tag_name)
        except NoSuchElementException:
            raise InavalidForAuthorError(
            f'Author {author_name} does not have any option with the {tag_name} tag'
        )    
        self.search_button.click()
        return self.quotes

class InavalidForAuthorError(ValueError):
    pass   


