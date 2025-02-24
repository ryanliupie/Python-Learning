# 'Amazon Website Scraping with Python'
# web scraping refers to an automated way of extracting and parsing data from the web using bots
# commonly used modules include Urllib2, Requests, BeautifulSoup, Lxml, Selenium, and MechanicalSoup
# py -m pip install requests
# py -m pip install bs4


# I want to know if the Macbook pro M4 base model will be under $2,200
import requests 
from bs4 import BeautifulSoup 

URL = 'https://www.amazon.ca/Apple-MacBook-Laptop-14%E2%80%91core-20%E2%80%91core/dp/B0DLHMYX53/ref=sr_1_2_sspa?crid=15572XBDCE8D&dib=eyJ2IjoiMSJ9.mTMEpIhJsjOVu0tWgZkBYERV02ripIEKs1QmYeVwQm1ckgBkkpGO0V2sjEwgSjISl7hPed5yHmmdVSGK1DuvLuF4ToI64XjWxv3wrtmuLDNqpCZSzccyPiIXAmybgTR54WnuGiOieTPp5jt-n7TMp9yvi2zVH1YV3_SJPoKJenMjk5kfWg8vVC8AuyZbBd6ZwmwZ9QCigEvGOsl3AlUnqTSRogDCsq4zpD6t7rXffl5fdUmuPZv-s46ux41Wy2FOLPKpQA1zQkAUJ56rZXAPvzOju86MXuj8y2dJw8Ios9Q.ZUGkGe5pCQlHNyXRnKQAmkaUqt2V7dVwNRcCg-3G0Ek&dib_tag=se&keywords=macbook%2Bpro%2Bm4&qid=1740362280&sprefix=macbook%2Bpro%2Bm%2Caps%2C164&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0'}

page = requests.get(URL, headers = headers)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())

product_title = soup.find(class_= 'product_title').get_text()
product_title = soup.find(class_= 'display_price').get_text()

print(product_title)