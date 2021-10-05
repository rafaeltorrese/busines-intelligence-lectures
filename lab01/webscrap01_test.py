import os
from  datetime import datetime


import requests
import lxml.html as html

URL_HOME = 'https://www.jornada.com.mx'
XPATH_LINKS = '//div[@class="flex-upper"]//h2[@class="title-default"]/a/@href'
XPATH_TITLE = '//div[@class="flex-upper"]//div[@class="card-title"]/h2[@class="title-default"]/a/text()'
XPATH_SUMMARY = '//div[@class="flex-upper"]//div[@class="card-text"]/p[1]/text()'
XPATH_BODY = '//div[@id="content_nitf"]/p/text()'
XPATH_ALL = '//div[@class="flex-upper"]'

response = requests.get(URL_HOME)
home = response.content.decode('utf-8')
parsed = html.fromstring(home)
links = parsed.xpath(XPATH_LINKS)

links_to_news = [f'{URL_HOME}{link}' for link in links]
titles = parsed.xpath(XPATH_TITLE)
summaries = parsed.xpath(XPATH_SUMMARY)


news = list(zip(links_to_news, titles, summaries))
print(len(news))


idx = 5
print(news[idx])
first_news = news[0]

print(first_news)


res = requests.get(first_news[0])
home_news = res.content.decode('utf-8')
parsed_news = html.fromstring(home_news)
body = parsed_news.xpath(XPATH_BODY)
print(type(body))
print(body)