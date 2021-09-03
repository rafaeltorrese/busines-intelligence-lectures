import os
from datetime import datetime

import requests
import lxml.html as html

URL_HOME = 'https://www.larepublica.co/'
XPATH_LINK_TO_ARTICLE = '//div[@class="news V_Title_Img"]/a[1]/@href'
XPATH_TITLE = '//text-fill/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p/text()'


def parse_news(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            news = response.content.decode('utf-8')
            parsed = html.fromstring(news)

            try:
                title = parsed.xpath(XPATH_TITLE)[0]
                title = title.replace('\"', '')
                summary = parsed.xpath(XPATH_SUMMARY)[0]
                body = parsed.xpath(XPATH_BODY)
            except IndexError:
                return 
            
            with open(f'{today}/{title}.txt', 'w', encoding='utf8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)


def parse_home():
    try:
        response = requests.get(URL_HOME)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parse = html.fromstring(home)
            links_to_notices = parse.xpath(XPATH_LINK_TO_ARTICLE)
            # print(links_to_notices)

            today = datetime.now().strftime('%Y-%m-%d')
            if not os.path.isdir(today):
                os.mkdir(today)
            
            for link in links_to_notices:
                parse_news(link, today)
            
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == '__main__':
    run()