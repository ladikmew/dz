import requests
from bs4 import BeautifulSoup

def Getting_News(url):
    all_news = []
    req = requests.get(url)
    src = BeautifulSoup(req.text, "html.parser")
    # print(src)
    for i in src.findAll('span', attrs={"class": "temp__value temp__value_with-unit"}):
        all_news.append(i.string)
        #   all_news.append('\n')
    return all_news[1]
# print(Getting_News("https://www.gismeteo.ru/weather-snezhinsk-11983/"))
print(Getting_News("https://yandex.ru/pogoda/sneginsk?lat=56.069252&lon=60.776794"))
