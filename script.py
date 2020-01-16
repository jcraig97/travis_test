from bs4 import BeautifulSoup
import requests

url = r'https://www.bbc.co.uk/news'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

title = soup.find('title')
print(title)