import requests
from bs4 import BeautifulSoup

url = "http://www.thehindu.com/news/national/canada-wont-support-separatist-movements-trudeau-tells-punjab-cm/article22816851.ece?homepage=true"
r = requests.get(url)

soup = BeautifulSoup(r.text,'lxml')
news = soup.find('div',{'id': 'content-body-14269002-22816851'})



for new in news:
    
    print(new)
    print()