from selenium import webdriver
from pages.quote_page import QuotePage


PATH = '/home/zaid/Desktop/Projects/Udemy/QuotePageScrapper/chromedriver_linux64/chromedriver'

chrome = webdriver.Chrome(executable_path = PATH)
chrome.get('http://quotes.toscrape.com/search.aspx')
page = QuotePage(chrome)

author = input("Enter the author you would like")
tag = input("Enter a tag")

page.select_author(author)
page.select_tag(tag)
page.search_button.click()


print(page.search_for_quotes(author,tag))


