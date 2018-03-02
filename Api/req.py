import requests
from bs4 import BeautifulSoup

url = "https://exploreflask.com/en/latest/"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
print()
print()

for link in soup.find_all('a'):
    print(link.get('href'))
