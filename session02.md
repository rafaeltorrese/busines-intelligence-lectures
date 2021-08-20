

Qué es HTTP. Protocolo, cojunto de reglas para comunicar dos pc

Status Code
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

HTML
https://www.w3schools.com/html/html_intro.asp


https://cadit.anahuac.mx/n/cadit-centro-de-alta-direccion-en-ingenieria-y-tecnologias
Tecla F12

robots.txt --> Define las reglas para poder extraer información de un sitio
https://www.anahuac.mx/mexico/robots.txt
User-agent: *  (Cualquier navegador, movil, algún script, etc.)


# XML Path Language
//div/span/h1[@class="title"][1]

# Tipos de nodos en XPath
Etiquetas HTML


https://toscrape.com/

Quotes / website
https://quotes.toscrape.com/

# Expresiones en XPath
F12 y click en console

- $x('/')  significa el root, selecciona todo el documento
- También significa un salto de nivel
- $x('/html')
- $x('//') salto entre nodos
- $x('//h1') Elegir todos los  headers en lugar de $x('/html/body/div')
- $x('//h1/text()')   --> Trae el texto del nodo. Esto en python es lo que se necesita.
- $x('//h1/text()').map(x => x.wholeText)
- $x('//h1/a/text()').map(x => xwholeText)  en la etiqueta a está el texto
- $x('//span/..')   ¿cómo accedo a todos los nodos padre ?	      
- $x('//span/.')   Nodo actual			  es igual a $x('//span')
- $x('//span/@class')   Extrae los atributos
- Cómo extraigo información con clases específicas? Esto se hace con predicados

# Predicados en XPath
- $x('/html/body/div/div')   Solo quiero un div
- $x('/html/body/div/div[1]')  Solo quiero el primer div de la lista
- $x('/html/body/div/div[last()]')  Otro predicado para traer el último div
- $x('//span[@class]')  Solo quiero etiquetas span con atributos class
- $x('//span[@class="text"]')   Atribtos de texto solamente
- $x('//span[class="text"]/text()')
- $x('//span[@class="text"]/text()').map(x => x.wholeText)  Todo el texto

# Operadores
1. $x('//span[@class!="text"]')  No text class
2. $('/html/body/div/div[position()=1]')
2. $('/html/body/div/div[position()>1]')
3. $x('//span[@class = "text" and @class="tag-item"]')
4. $x('//span[@class = "text" or @class="tag-item"]')
5. $x('//span[not(@class)]')  negación

# Wildcard
1. $x('/*')
2. $x('/html/*')
3. $x('//*')  preguntar qué obtienen, todos los nodos en todas las direcciones
4. $x('//span[@class="text"]/@*')  Todos los atributos de los nodos span que tiene clase text
5. $x('/html/body//div/@*') Todos los atributos que tienen los div
6. $x('//sapan[@class="text" and @itempro="text"]/node()') Todos los "span" que tengan una clase de texto, además estos span quiero que tengan atributos. Node trae además de los nodos lo que está más allá.

# In-text Search en XPath
1. $x('//small[@class="author" and starts-with(.,"A")]')  Nodo actual
2. $x('//small[@class="author" and starts-with(., "A")]/text()').map(x => x.wholeText)
3. $x('//small[@class="author" and contains(., "Ro")]')
4. $x('//small[@class="author" and contains(., "Ro")]/text()').map(x => x.wholeText)
5. $x('//small[@class="author" and ends-with(., "t")]').map(x => x.wholeText)  Error por la versión de Xpath 1.0 ésta función corresponde a la version 2.0
6. $x('//small[@class="author" and matches(., " ")]/text()').map(x => x.wholeText)
7. $x('//small[@class="author" and starts-with(.,"e")]/text()')
8. $x('//small[@class="author" and starts-with(., "a")]/text()').map(x => x.wholeText)
9. $x('//small[@class="author" and stars-with(.,"E")]/text()').map(x => x.wholeText)

# XPath Axes
1. $x('/html/body/div')
2. $x('/html/body/div/.')
3. $x('/html/body/div/self::div')
4. $x('/html/body/div/child::div')  Todos los hijos
5. $x('/html/body/div/descendant::div') Todos los nietos
6. $x('/html/body/div/descendant-or-self::div') Todos los nietos y él mismo

# Exercise
Ir a Books https://books.toscrape.com/
1. Ir a elements y seleccionar un título
2. Están en nodo <a >
3. $x('//article[@class="product_pod"]/h3/a[@title]/text()').map(x => x.wholeText)
4. $x('//article[@class="product_pod"]/h3/a/@title').map(x => x.value) Expresión equivalente a punto 3
5. Ahora los precios
6. $x('//article[@class="product_pod"]//p[class="price_color"]/text()').map(x => x.wholeText)
7. $x('//article[@class="product_pod"]/div[@class="product_price"]/p[@class="price_color"]/text()').map(x => x.wholeText) Equivalente a punto 6
8. Categoría de libros
9. $x('//div[@class="side_categories"]/ul[@class="nav nav-list"]/li/ul/li/a/text()').map(x => x.wholeText)

# Challenge
1. Libro. Extraer descripción y stock disponible
2. $x('//article[@class="product_page"]/p/text()').map(x => x.wholeText) 
2. $x('//div[@class="col-sm-6 product_main"]/p[@class="instock availability"]/text()').map(x => x.wholeText)

# Project
https://www.larepublica.co/empresas/segunda-edicion-de-la-feria-de-carros-usados-de-automoviles-abondano-sera-el-domingo-3219575
1. $x('//h2[@data-h="16"]/a/@href').map(x => x.value)
2. Guardar en archivo xpath.txt la siguiente expresión
  - Links = //h2[@data-h="16"]/a/@href
3. $x('//h2[@data-h="45"]/span/text()').map(x => x.wholeText)
  - Titulo = //h2[@data-h="45"]/span/text()
4. $x('//div[@class="lead"]/p/text()').map(x => x.wholeText)
  - //div[@class="lead"]/p/text()
5. $x('//div[@class="lead"]/p/text()').map(x => x.wholeText)
  - Resumen = //div[@class="lead"]/p/text()
6. $x('//div[@class="html-content"]/p[not(@class)]/text()').map(x => x.wholeText)
  - Cuerpo = //div[@class="html-content"]/p[not(@class)]/text()

# Python
1. import requests
2. import lxml.html as html
3. import autopep8


