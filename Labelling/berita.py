import requests
import datetime as dt
from bs4 import BeautifulSoup

date = dt.datetime.today

url = 'https://www.detik.com/search/searchall?query=rohingya+di+aceh&sortby=time&page'
#print (url)
page = requests.get(url)
#print (page)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)
articles = soup.find_all('div', class_= 'list media_row list-berita')
print(articles)
for article in articles:
    title = article.find('article').text.strip()
    #print(title)