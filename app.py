from selenium import webdriver
from pages.quote_page import QuotePage


PATH = '/home/zaid/Desktop/Projects/Udemy/QuotePageScrapper/chromedriver_linux64/chromedriver'

chrome = webdriver.Chrome(executable_path = PATH)
chrome.get('http://quotes.toscrape.com/search.aspx')
page = QuotePage(chrome)

author  = input("enter the author name : ")
page.select_author(author)
