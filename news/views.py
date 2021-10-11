from django.shortcuts import render

import requests
from bs4 import BeautifulSoup



#times of india scraping part 

india_news = requests.get("https://timesofindia.indiatimes.com/briefs")
soup = BeautifulSoup(india_news.content,"html5lib")

headings = soup.find_all('h2')
headings = headings[0:15]

toi_news = []

for i in headings:
    toi_news.append(i.text)


#yahoo news scraping part

yahoo = requests.get("https://news.yahoo.com/")
yahoo_soup = BeautifulSoup(yahoo.content,"html5lib")

yahoo_headings = yahoo_soup.find_all('h3',class_="Mb(5px)")
yahoo_headings = yahoo_headings[0:13]

news = []

for i in yahoo_headings:
    news.append(i.text)

    
def index(request):
        return render(request,'index.html',{'toi_news':toi_news,'news':news})





