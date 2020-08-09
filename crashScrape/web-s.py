from selenium import webdriver
from bs4 import BeautifulSoup as soup
import pandas as pd

from urllib.request import Request, urlopen as uReq
import requests 

req = Request('https://roobet.com/crash', headers={'User-Agent': 'Mozilla/5.0'})

#open connection and grab page
webpage = uReq(req)
page_html = webpage.read()

#html parsing
page_soup = soup(page_html,'html.parser')



#set webdriver path
driver = webdriver.Chrome("/usr/local/bin/geckodriver")

#get url data
driver.get("https://roobet.com/crash")

driver.find_element_by_class_name('jss108')

js= Document.getElementsByClassName()


# products=[] #List to store name of the product
# prices=[] #List to store price of the product
# ratings=[] #List to store rating of the product
# driver.get("https://roobet.com/crash")

#driver.get("<a href="https://www.flipkart.com/laptops/">https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq")


# content = driver.page_source
# soup = BeautifulSoup(content)
# for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
#     name=a.find('div', attrs={'class':'_3wU53n'})
# price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
# rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
# products.append(name.text)
# prices.append(price.text)
# ratings.append(rating.text) 

