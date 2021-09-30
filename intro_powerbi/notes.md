# Download PowerBI

https://powerbi.microsoft.com/en-us/downloads/
https://aka.ms/pbidesktopstore

# Tipos de Análisis

¿Cuántas ventas se hicieron en el Q2 del 2018?
¿Cuáles son las 10 regiones ?

¿Qué eventos detonaron más ventas?
¿Qué situaciones recurrentes afectan nuestra operación?

# Visualización de datos

Fuente: https://veja.abril.com.br/blog/radar/perfil-do-psdb-distorce-popularidade-de-doria/
Mala representación de la escala. Dice 22% y la escala se ve a 90%
Voto nulo está casi al final. Hay sesgo en la decisión.
Los colores se repiten

## Elemementos para mejorar PowerBI

Color. Ayuda a representar escalas. Resaltar datos importantes. Por ejemplo si es algo negativo lo pones en rojo si es positivo en color azul.
Color amarillo y los demás elementos en color gris para las gráfica de barras del candidato
Ordenar los objetos. Mayor a menor por ejemplo.
Correcta selección de visualización.

- La visualización no debe confundir o distorsionar
- Cuidar el resultado estético de un informe. Tamañao de letra, colores, etc. La lectura debe ser suave

# Power BI

Load DataSet CSV "olist_customers_dataset.csv"
Change to UTF-8
Load DataSet
Load DataSet CSV "olist_orders_dataset.csv"
Change DateTime to Date. - TransformData. PowerQuery Manipualates Data without changing original data. - Select column "order_purchase_timestamp" - Right click and Transform - Select Date Only

- close and apply

# Reports with PowerBI

¿Cuántos clientes tenemos?. Podemos hacer esta consulta de acuerdo a un lapso de tiempo o histórico
customers_dataset -> customer_id

Answers
¿Cuántas ventas tuvimos en 2017?
¿Comparativo de ventas 2017 y 2018?
Go to Models and see orders\*dataset

- Inform Module
- oil_customers_dataset
- drag and droo 'dataset->order_id'
- Visualizations -->  Card
- Click on fields
  - Select count (distinct)
- Click on Format
  - DataLabel
    - Color
    - Diplay Units: None
  - Title: Customers' Company
  - Category Label
- orders_dataset --> order_id (select, drag and drop)
- orders_dataset --> order_purchase_timestamp (select, drag and drop)
- Visualizations --> bars
- orders_dataset --> order_id (select, drag and drop)
- orders_dataset --> order_purchase_timestamp (select, drag and drop)
- Visualizations --> bars 
  - Filters --> Year

# Edición datos PowerQuery

- Transform Data Menu
- 'order_items_datasets' (table)
- ¿Cuánto están pagando clientes por un producto?
- sum price and fright_value
- click on columns price and friht_value (shift to select both colums)
- Add column (menu)
- Standard / Add
- change column labels:
  - Price
  - Freight Cost
  - Delivery Time
- change table name
  - Order Elements
- Elements Order
  - order_id
  - Total Price
- ¿Cuál es el precio total que más se frecuenta en la compra de un producto?
  - order_id drag on value
  - Total Price drag on Axis
- Filter on 'Total Price'
  - Advanced Filter
  - Greater than 1100
  - Less than 1200
  - Hover the mouse over one bar
- Add data our object. Freight Cost and Price Product
- From 'Order Elements' select Price and Freight Cost
- Visualizations / Tools Tips

# Typical Errors Using Power BI
- No se establece el tipo de dato
- Datos sucios. Símbolos que confunden a PowerBI
- Go To: Transform
  - New Origin
  - Import Wheter_RJ_SP.xlsx --> Select RJ 2018 --> Accept
  - On the header Min and Max are identified as strings ¿why? Because of Celsius Symbol.
  - Click on 'Min' Column then click on Transform Tab --> Extract --> First Characters --> 2 first characters
  - Right Click on the column --> Change Type --> Integer
  - Home --> Close and Apply
  - The Higher Temperature the higher volume sales
  - March Temperatures in Sao Paolo and the Sales.
    - Add new page
    - Select Weather_RJ_2018
    - Select Date and Max fields
    - Click on the next hierarchy level twice (day level)
    - Filters --> 2018 --> March
    - Go to Fields (right panel) --> City
    - Drag on Filters --> Click Sao Paolo
  - Sales on the same city
    - 'olist_orders_dataset'
      - Select order_id
      - order_purchase_timestamp
    - Select 'olist_customers_dataset'
      - customer_city
    - Go to visulizations
      - select stack plot
      - Value: Recount order_id
      - Filters --> sao paulo
      - Down hiearchy level to trimesters. Go to march.
      - Filters --> timestamp 2018 and only march

# Connect DataBase PowerBI DirectQuery
- Import vs Connect
- High Frequency Changing
- Time Query 5 seconds Parameters between DirectQuery and DB
- DirectQuery easy to query big data
- Security Management