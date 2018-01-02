from bs4 import BeautifulSoup
import requests

res = requests.get ('http://quotes.toscrape.com/page/2/')
soup = BeautifulSoup (res.text, 'lxml')
quote = soup.find_all ('span', {'class': 'text'})
for q in quote:
    print (q.text)
