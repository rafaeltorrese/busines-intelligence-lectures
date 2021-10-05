#%%
import requests
from bs4 import BeautifulSoup
from pprint import pprint
#%%

URL = 'https://www.jornada.com.mx'

# class="nav-link"
# class="extra-item item-cultura"
# class="extra-item"


# sections
# li class="nav-item"
# class="nav-link"

home = requests.get(URL)

soup_home = BeautifulSoup(home.text, 'lxml')


sections01 = soup_home.find('ul', attrs={'class':"navbar-nav mr-auto text-uppercase"}).find_all('li')[:-1]
section_links = [URL + section.find('a').get('href') for section in sections01]


more_sections = soup_home.find('ul', attrs={'class':"navbar-nav mr-auto text-uppercase"}).find_all('li')[-1]
more_sections_left = more_sections.find('div', attrs={'class': "left"}).find_all('a')
more_sections_right = more_sections.find('div', attrs={'class': "right"}).find_all('a')

section_left_links = [URL + section.get('href') for section in more_sections_left[3:-1] ] 
section_right_links = [section.get('href') if section.get('href').startswith('http') else URL + section.get('href') for section in more_sections_right]

links = section_links + section_left_links + section_right_links
#%%
print(links[0])
first_section = requests.get(links[0])

soup_first_section = BeautifulSoup(first_section.text, 'lxml')
#%%
featured_article = soup_first_section.find('div', attrs={'class': "card-body"}).find('div', attrs={'class': "flex-upper"}).find('h2', attrs={'class': "title-default"}).find('a')

print(featured_article)