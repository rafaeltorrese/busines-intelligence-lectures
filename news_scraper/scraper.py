import requests
import lxml.html as html

URL_HOME = 'https://www.larepublica.co/'
XPATH_LINK_TO_ARTICLE = '//div[@class="news V_Title_Img"]/a/@href'
XPATH_TITLE = '//h2[@data-h="45"]/span/text()'
XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p/text()'

def parse_home():
    try:
        response = requests.get(URL_HOME)
        if response.status_code == 200:
            home = response.content.decode('utf-8')
            parse = html.fromstring(home)
            links_to_notices = parse.xpath(XPATH_LINK_TO_ARTICLE)
            print(links_to_notices)
            
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == '__main__':
    run()