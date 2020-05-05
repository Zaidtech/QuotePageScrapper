from selenium import webdriver
from pages.quote_page import QuotePage


PATH = '/home/zaid/Desktop/Projects/Udemy/QuotePageScrapper/chromedriver_linux64/chromedriver'

chrome = webdriver.Chrome(executable_path = PATH)
chrome.get('http://quotes.toscrape.com/')
page = QuotePage(chrome)

for quote in page.quotes:
  print(quote)
