# %%
from IPython.display import Image
import requests
from bs4 import BeautifulSoup
from pprint import pprint

from auxfunc import get_notes
# %%


def my_links_section(url, section):
    featured_article = section.find('section', attrs={'class': "top-content"})
    featured_article_link = url+featured_article.a.get('href')
    article_list = section.find_all(
        'h4', attrs={'class': "is-display-inline title-list"})
    article_links = [featured_article_link] + \
        [f"{url}{article.a.get('href')}" for article in article_list]

    return article_links

#%%
def get_info(soup_note):
    info = {
        'date': None,
        'title': None,
        'teaser': None,
        'subheader': None,
        'author': None,
        'body': None,
        'image': None,
        }

    date = soup_note.find('time').get('datetime')
    if date:
        info['date'] = date.split('T')[0]

    title = soup_note.find('div', attrs={'class': "col 2-col"}).find('h1')
    if title:
        info['title'] = title.get_text()

    # volanta
    teaser = soup_note.find(
        'div', attrs={'class': "col 2-col"}).find('h4')  # maybe None
    if teaser:
        info['teaser'] = teaser.get_text()

    # copete o bajada
    subheader = soup_note.find(
        'div', attrs={'class': "col 2-col"}).find('h3')  # maybe None
    if subheader:
        info['subheader'] = subheader.get_text()

    # author
    author = soup_note.find('div', attrs={'class': "author-name"})
    if author:
        info['author'] = author.get_text()

    # body
    body = soup_note.find(
        'div', attrs={'class': "article-main-content article-text"}).find_all('p')
    body_text = [b.get_text() for b in body]
    if body:
        info['body'] = body_text[0]
    
    # media
    img = soup_note.find('figure', attrs={
    'class': "object-fit-block--contain intrinsic-container intrinsic-container-3x2"}).find('img')
    
    if img:
        img_src = img.get('data-src')
        try:
            img_request = requests.get(img_src)
            if img_request.status_code == 200:
                info['image'] = img_request.content
        except :
            print('Image was not found')
    else:
        print('There is no media image')
    
    return info
#%%
def scrap_note(url):
    try:
        note = requests.get(url)
    except Exception as e:
        print(f'Error scraping URL {url}')
        print(e)
        return None
    if note.status_code != 200:
        print(f'Error in note {url}')
        print(f'Status Code {note.status_code}')
        return None
    
    soup_note = BeautifulSoup(note.text, 'lxml')
    
    info_dict = get_info(soup_note)
    info_dict['url'] = url

    return info_dict

# %%
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

print(p12.request.url)

s = BeautifulSoup(p12.text, 'lxml')
# print(type(s))
# %%
# print(s.prettify())
# %%
# print(s.find('ul'))  # first element

# print(s.find('ul', attrs={'class': "horizontal-list main-sections hide-on-dropdown"}).find_all('li'))

# %% [markdown]
# # EXTRACT INFO
# %%
sections = s.find('ul',
                  attrs={
                      'class': "horizontal-list main-sections hide-on-dropdown"}).find_all('li')
print(sections)
# %%
print(sections[0])

section = sections[0]

print(section)

print(section.find('a'))

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

# %%
article_list = s_sec.find_all(
    'h4', attrs={'class': "is-display-inline title-list"})

pprint(article_list)
# print(len(article_list))
# %%
print(url+article_list[0].a.get('href'))

article_links = [f"{url}{article.a.get('href')}" for article in article_list]
print(len(article_links))
print(article_links)
print(len(article_links))

# print(my_links_section(url, s_sec))
# print(get_notes(url, s_sec))


# %% [markdown]
# ## Exceptions
# %%
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

# %%
print(note_list)
url_note = note_list[0]
print(url_note)
# %%
try:
    note = requests.get(url_note)
    if note.status_code == 200:
        s_note = BeautifulSoup(note.text, 'lxml')
        # Title
        title = s_note.find('div', attrs={'class': "col 2-col"}).find('h1')
        print(title.text)
        
        date = s_note.find('time').get('datetime')
        print(date.split('T')[0])

        # volanta
        teaser = s_note.find(
            'div', attrs={'class': "col 2-col"}).find('h4')  # maybe None
        # print(teaser.text)
        print(teaser.get_text())

        subheader = s_note.find(
            'div', attrs={'class': "col 2-col"}).find('h3')  # maybe None

        print(subheader.get_text())

        author = s_note.find('div', attrs={'class': "author-name"})
        # print(author.text)

        body = s_note.find(
            'div', attrs={'class': "article-main-content article-text"}).find_all('p')

        # print(body)

except Exception as e:
    print(f'Error {e}', '\n')
# %%
media = s_note.find('figure', attrs={
    'class': "object-fit-block--contain intrinsic-container intrinsic-container-3x2"}).find('img')
print(media)
# %%
media_src = media.get('data-src')
print(media_src)
# %%
img_req = requests.get(media_src)
# %%
print(img_req.status_code == 200)
# %%
img_req.content
# %%

Image(img_req.content)
# %%
print(url_note)
#%%
print(scrap_note(url_note))
# %%
print(links_sections)
# %%
notes = []
for link in links_sections:
    try:
        r = requests.get(link)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, 'lxml')
            notes.extend(get_notes(url, soup))
        else:
            print('Section was not found')
    except:
        print('Section was not found', link)

# %%
print(notes)
# %%
data = []
for i, note in enumerate(notes, 1):
    print(f'Scraping note {i} / {len(notes)}')
    data.append(scrap_note(note))
# %%
print(len(data))
# %%
import pandas as pd
# %%
df = pd.DataFrame(data)
# %%
print(df.head())
# %%
df.to_csv('NotesPage12.csv')
# %%
