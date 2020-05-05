from selenium import webdriver
from pages.quote_page import QuotePage, search_for_quote


PATH = '/home/zaid/Desktop/Projects/Udemy/QuotePageScrapper/chromedriver_linux64/chromedriver'

chrome = webdriver.Chrome(executable_path = PATH)
chrome.get('http://quotes.toscrape.com/search.aspx')
page = QuotePage(chrome)

author = input("Enter the author you would like ")
selected_tag = input("Enter a tag")

page.select_tag(selected_tag)
page.search_button.click()
page.select_author(author)

print(page.search_for_quote(author,selected_tag))


