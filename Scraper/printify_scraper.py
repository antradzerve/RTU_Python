import requests 
from bs4 import BeautifulSoup

page = requests.get("https://printify.com/app/products")
print(page)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())