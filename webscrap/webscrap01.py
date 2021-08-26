#%%
import requests
from bs4 import BeautifulSoup
from pprint import pprint

from auxfunc import get_notes
#%%

def my_links_section(url, section):
    featured_article = section.find('section', attrs={'class': "top-content"})
    featured_article_link = url+featured_article.a.get('href')
    article_list = section.find_all('h4', attrs={'class':"is-display-inline title-list"})
    article_links =  [featured_article_link] + [f"{url}{article.a.get('href')}" for article in article_list]

    return  article_links

#%%
url = 'https://www.pagina12.com.ar'


# print(requests.get(url))
p12 = requests.get(url)

# Codigo Status HTTP
# print(p12.status_code)
# print(p12.text)

# print(p12.content)  # photos, audio, etc

# print(p12.headers)  # response from the server

# print(p12.request.headers)  # headers output, from my pc

# print(p12.request.method)

print(p12.request.url)  #  

s = BeautifulSoup(p12.text, 'lxml')
# print(type(s))
#%%
# print(s.prettify())
# %%
# print(s.find('ul'))  # first element

# print(s.find('ul', attrs={'class': "horizontal-list main-sections hide-on-dropdown"}).find_all('li'))

#%% [markdown]
# # EXTRACT INFO

sections = s.find('ul', 
            attrs={
                'class': "horizontal-list main-sections hide-on-dropdown"}).find_all('li')
# %%
# print(sections[0])

section = sections[0]

# print(section)

# print(section.find('a'))

# print(section.a)

# Title
# print(section.a.get('href'))
# print(section.a.text)
# print(section.a.get_text())

links_sections = [section.a.get('href') for section in sections]

# print(links_sections)

sec = requests.get(links_sections[0])
# print(links_sections[0])
# print(sec)
s_sec = BeautifulSoup(sec.text, 'lxml')
# print(s_sec)
# print(s_sec.prettify())

featured_article = s_sec.find('section', attrs={'class': "top-content"})
print()
# print(url+featured_article.a.get('href'))

article_list = s_sec.find_all('h4', attrs={'class':"is-display-inline title-list"})


# pprint(article_list)
# print(len(article_list))

# print(url+article_list[0].a.get('href'))

article_links = [f"{url}{article.a.get('href')}" for article in article_list]
# print(len(article_links))
# print(article_links)


# print(my_links_section(url, s_sec))
print(get_notes(url, s_sec))


#%% [markdown]
# ## Exceptions
r = requests.get(url)
print(r)

if r.status_code == 200:
    pass
else:
    raise ValueError(f'Error {r.status_code}')

url_mala = url.replace("2", "3")

try:
    print(requests.get(url_mala))
except Exception as e:
    print('Request Error')
    print(e, '\n')

note_list = get_notes(url, s_sec)
url_note = note_list[0]
print(url_note)

try:
    note = requests.get(url_note)
    if note.status_code == 200:
        s_note = BeautifulSoup(note.text, 'lxml')
        # Title
        
except Error as e:
    print(f'Error {e}', '\n')