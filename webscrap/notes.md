# HTML. Requests and BeautifulSoup
[BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
## Downloading HTML
url = 'https://www.pagina12.com.ar'
print(requests.get(url))
p12 = requests.get(url)
Codigo Status HTTP
print(p12.status_code)
print(p12.text)
Media content
    print(p12.content) 
Response from the server
    print(p12.headers)
Headers output, from my pc
    `print(p12.request.headers)  `
Different Methods (Get, Put, Delete)
    `print(p12.request.method)`
print(p12.request.url) 

## Parsing a HTML file with BeautifulSoup
1. Change to virtual environment
2. Initialize virtual environment: conda activate bi
3. Launch VSCode and set the kernel. Use de bi virtual environment
4. Create a new file webscrap01.py
### Code
1. from bs4 import BeautifulSoup
2. print(BeautifulSoup(p12.text, 'lxml'))
3. s = BeautifulSoup(p12.text, 'lxml')
4. print(type(s))
5. print(s.prettify())
6. extract news section
7. inspect elements and look up for sections
8. `<a href="https://www.pagina12.com.ar/secciones/el-pais">El país</a>`
9. `<a href="https://www.pagina12.com.ar/secciones/economia">Economía</a>`
10. 
```
    <ul class="horizontal-list main-sections hide-on-dropdown">
        <li class="  p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/el-pais">El país</a></li>
        <li class="  p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/economia">Economía</a></li>
        <li class="  p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/sociedad">Sociedad</a></li>
        <li class=" no-separator-on-1040 p12-separator--right--primary"><a href="https://www.pagina12.com.ar/suplementos/cultura-y-espectaculos">Cultura y Espectáculos</a></li>
        <li class="hide-on-1040  p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/deportes">Deportes</a></li>
        <li class="hide-on-1040  p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/el-mundo">El mundo</a></li>
        <li class="hide-on-1040  "><a href="https://www.pagina12.com.ar/secciones/cultura">Cultura</a></li>        
    </ul>

```    
11. s.find('ul') returns the first element tha was found
12. s.find('ul', attrs={
                    'class': "horizontal-list main-sections hide-on-dropdown",
                    })
13. s.find('ul', attrs={
                    'class': "horizontal-list main-sections hide-on-dropdown",
                    }).find_all('li')

14. print(s.find('ul', attrs={
                    'class': "horizontal-list main-sections hide-on-dropdown",
                    }).find_all('li'))

## Extract Info
1. sections = s.find('ul', attrs={
                                'class': "horizontal-list main-sections hide-on-dropdown",
                            }).find_all('li')
1. print(sections[0])
    `<li class="  p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/el-pais">El país</a></li>`
1. section = sections[0]
1. print(section.find('a'))
    `<a href="https://www.pagina12.com.ar/secciones/el-pais">El país</a>`
`section.find('a')` is the same as `section.a`
1. print(section.a)
1. Seek for the title and the link in the a element
    `section.a.get_text()`
        'El país'
    `section.a.get('href')`
        "https://www.pagina12.com.ar/secciones/el-pais"

1. create a variable to store the section links
    `section_links = [section.a.get('href') for section in sections]`
1. print(section_links)
1. Repeat the process for each url in `section_links`
    ```python
    print(section_links[0])
    print(requests.get(section_links[0]))
    sec = requests.get(section_links[0])
    ```
1. print(sec)
1. Print the status code of de `sec` variable `print(sec.status_code)`
1. Parsing with BS
```python
    print(BeautifulSoup(sec, 'lxml'))
    soup_section = BeautifulSoup(sec, 'lxml')
    print(soup_section.prettify())
```
1. We obtain a different web page,this new page corresponds to a section, for example: https://www.pagina12.com.ar/secciones/el-pais
1. We are interested in the links for each news or notes. We only need the information.
1. Our Featured Article is inside the `<section class="top-content" id="top-content">`
1. Get the element
```
   soup_section.find('section', attrs={
                                        'class': "top-content",
                                        })
    featured_article = soup_section.find('section', attrs={'class': "top-content"})
    print(featured_article)
    print(url+featured_article.a.get('href'))
```
1. Obtaining the reste of the notes
```python
article_list = soup_section.find_all('h4', attrs={'class': "is-display-inline title-list"})
print(article_list)
print(url+article_list[0].a.get('href'))
article_links = [f"{url}{article.a.get('href')}" for article in article_list]
print(len(article_links))
print(article_links)
```
1. Create a function in another file
```python
def get_notes(url, section):
    '''
    Function that returns a URL list to the notes in a section
    '''
    featured_article = section.find('section', attrs={'class': "top-content"})
    
    featured_link = url+featured_article.a.get('href') if featured_article else  None
    
    article_list = section.find_all('h4', attrs={'class':"is-display-inline title-list"})

    if featured_link:
        return [featured_link] + [f"{url}{article.a.get('href')}" for article in article_list if article]
    
    return [f"{url}{article.a.get('href')}" for article in article_list if article]
```

## Handling Errors
1. `r = requests.get(url)`
1. 
```python
print(r)
if r.status_code == 200:
    # processing request
else:
    # print the error    

```
1. Introduce an error
```python
bad_url = url.replace('2', '3')
print(bad_url)
print(requests.get(bad_url))
```
1. Handling errors
```python
try:
    requests.get(bad_url)
except:
    print('Error')
```
1. Another handling error, add the `Exception` object
```python
try:
    requests.get(bad_url)
except Exception as e:
    print('Error')
    print(e)
    print('\n')
```
1. 
```python
try:
    featured_article.b.get('href')
except:
    print('Continue')
print('Code still running')
```


## Content Downloading 
1. Save one link from the link list
```python
url_note = article_links[0]
print(url_note)
```
2. Extract the title and the date. Inspect the news for these elements. 

```python
try:
    note = requests.get(url_note)
    if note.status_code == 200:
        soup_note = BeautifulSoup(note.text, 'lxml')
        # Extract title
        title = soup_note.find('div', attrs={'class': "col 2-col"}).find('h1')
        print(title)
        date = soup_note.find('div', attrs={'class': "date"}).find('span')

        # Extract volanta
        teaser = soup_note.find('div', attrs={'class': "col 2-col"}).find('h4')
        print(teaser.text)
        print(teaser.get_text())

        subheader = soup_note.find('div', attrs={'class': "col 2-col"}).find('h3')
        
        author = soup_note.find('div', attrs={'class': "author-name"})
        body =  soup_note.find('main')

        body = soup_note.find(
            'div', attrs={'class': "article-main-content article-text"}).find_all('p')

        print(body)
except Exception as e:
    print('Error: ')
    print(e)
    print('\n')
```

## Media Content
media = soup_note.find()
## Scraper as a whole

