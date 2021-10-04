import os
from  datetime import datetime

import requests
import lxml.html as html

URL_HOME = 'https://www.jornada.com.mx'
XPATH_LINKS = '//div[@class="flex-upper"]//h2[@class="title-default"]/a/@href'
XPATH_TITLE = '//div[@class="flex-upper"]//div[@class="card-title"]/h2[@class="title-default"]/a/text()'
XPATH_SUMMARY = '//div[@class="flex-upper"]//div[@class="card-text"]/p[1]/text()'
XPATH_BODY = '//div[@id="content_nitf"]/p/text()'


def parse_notes(note, number,  date):
    try:
        response = requests.get(note[0])  # if the url is ath first position of the list
        if response.status_code == 200:
            news = response.content.decode('utf-8')
            parser = html.fromstring(news)
            
            try:
                title = note[1].replace('\"', '').replace("'",'').replace(':', ' ').replace('/', ' ').strip()
                summary = note[2].strip()
                body_list = parser.xpath(XPATH_BODY)
            except IndexError:
                return
            
            with open(f'{date}/{str(number).zfill(2)}-{title}.txt',  'w', newline='',  encoding='utf8') as file:
                file.write(title)
                file.write('\n\n')
                file.write(summary)
                file.write('\n\n')
                for p in body_list:
                    file.write(p)
        else:
            raise ValueError(f'Error: {response.status_code}') 

    except ValueError as ve:
        print(ve)



def parse_home(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parser = html.fromstring(home)

            links = parser.xpath(XPATH_LINKS)
            links_to_news = [f'{URL_HOME}{link}' for link in links]
            titles = parser.xpath(XPATH_TITLE)
            summaries = parser.xpath(XPATH_SUMMARY)
            
            newslist = list(zip(links_to_news, titles, summaries))

            today = datetime.now().strftime('%Y-%m-%d')

            if not os.path.isdir(today):
                os.mkdir(today)

            total_news = len(newslist)
            for i, news in enumerate(newslist, 1):
                parse_notes(news, i, today)
        
        else:
            raise ValueError(f'Error: {response.status_code}')

    except ValueError as ve:
        print(f'Error: {ve}')


def run(url):
    parse_home(url)

if __name__ == '__main__':
    run(URL_HOME)