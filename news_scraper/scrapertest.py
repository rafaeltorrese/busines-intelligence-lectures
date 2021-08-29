import requests 
import lxml.html as html

URL_HOME = 'https://www.larepublica.co/'
XPATH_LINK_TO_ARTICLE = '//div[@class="news V_Title_Img"]/a/@href'

# XPATH_TITLE = '//h2[@data-h="45" and @style="font-size: 45px; line-height: 49px;"]/span/text()'
# XPATH_TITLE = '//div[@data-epica-module-name="Contenido"]/div[position() = 1]/div[2]/div[1]/span'
# XPATH_TITLE = '//div[@data-epica-module-name="Contenido"]'
# XPATH_TITLE = '//div[@data-epica-module-name="Contenido"]//div[@class="mb-auto"]/node()'  #

# XPATH_TITLE = '//div[@data-epica-module-name="Contenido"]//div[@class="mb-auto"]/text-fill/span/text()'
XPATH_TITLE = '//text-fill/span/text()'

# XPATH_TITLE = '//*[@id="vue-container"]/div[3]/div[1]/div[2]/div[1]/text-fill/span/text()'  # ok
# XPATH_TITLE = '//*[@id="vue-container"]/div[3]/div[1]/div[2]/div[1]/h2/span/text()'  # NOP (COPY AND PASTE FROM CONTEXTUAL MENU)

XPATH_SUMMARY = '//div[@class="lead"]/p/text()'
XPATH_BODY = '//div[@class="html-content"]/p/text()'

# //*[@id="vue-container"]/div[3]/div[1]/div[2]/div[1]/h2/span/text()
response = requests.get(URL_HOME)

# see status code
# print(response.status_code)

home = response.content.decode('utf-8')
# print(home)
parsed = html.fromstring(home)
# print(parsed)

# print(parsed.xpath(XPATH_LINK_TO_ARTICLE))
links_to_news = parsed.xpath(XPATH_LINK_TO_ARTICLE)
# print(type(links_to_news))
# print(len(links_to_news))
# print(links_to_news)

#%% [markdown]
# ## Single News
first_link = links_to_news[0]
print(first_link)
# print(requests.get(first_link).status_code)
res = requests.get(first_link)
# print(res.status_code)

news = res.content.decode('utf-8')
# print(news)
par = html.fromstring(news)
# print(par)

#%% [markdown]
# ## Title, Summary, Body
print(par.xpath(XPATH_TITLE))  # OK
# print(par.xpath(XPATH_SUMMARY))  ok
# print(par.xpath(XPATH_BODY)) ok
