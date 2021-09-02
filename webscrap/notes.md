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
8. <a href="https://www.pagina12.com.ar/secciones/el-pais">El país</a>
9. <a href="https://www.pagina12.com.ar/secciones/economia">Economía</a>
10. <ul class="horizontal-list main-sections hide-on-dropdown">
        1. <li class="  p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/el-pais">El país</a></li>
        2. <li class="  p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/economia">Economía</a></li>
        3. <li class="  p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/sociedad">Sociedad</a></li>
        4. <li class=" no-separator-on-1040 p12-separator--right--primary"><a href="https://www.pagina12.com.ar/suplementos/cultura-y-espectaculos">Cultura y Espectáculos</a></li>
        5. <li class="hide-on-1040  p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/deportes">Deportes</a></li>
        6. <li class="hide-on-1040  p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/el-mundo">El mundo</a></li>
        7. <li class="hide-on-1040  "><a href="https://www.pagina12.com.ar/secciones/cultura">Cultura</a></li>
    </ul>
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
sections = s.find('ul', attrs={
                                'class': "horizontal-list main-sections hide-on-dropdown",
                            }).find_all('li')
print(sections[0])
    `<li class="  p12-separator--right--primary"><a href="https://www.pagina12.com.ar/secciones/el-pais">El país</a></li>`
section = sections[0]
print(section.find('a'))
    `<a href="https://www.pagina12.com.ar/secciones/el-pais">El país</a>`
`section.find('a')` is the same as `section.a`
print(section.a)
Seek for the title and the link in the a element
    `section.a.get_text()`
        'El país'
    `section.a.get('href')`
        "https://www.pagina12.com.ar/secciones/el-pais"

create a variable to store the section links
    `section_links = [section.a.get('href') for section in sections]`
print(section_links)
Repeat the process for each url in `section_links`
    ```python
    print(section_links[0])
    print(requests.get(section_links[0]))
    sec = requests.get(section_links[0])
    ```
print(sec)
print(sec.status_code)
Parsing with BS
```python
    print(BeautifulSoup(sec, 'lxml'))
    soup_section = BeautifulSoup(sec, 'lxml')
    print(soup_section.prettify())
```
We obtain a different web page,this new page corresponds to a section, for example: https://www.pagina12.com.ar/secciones/el-pais
We are interested in the links for each news or notes. We only need the information.
Our Featured Article is inside the `<section class="top-content" id="top-content">`
Get the element
    soup_section.find('section', attrs={
                                        'class': "top-content",
                                        })
    featured_article = soup_section.find('section', attrs={'class': "top-content"})
    print(featured_article)
    <h2 class="title-list">

## Handling Errors

## Content Downloading 


## Media Content

## Scraper as a whole

