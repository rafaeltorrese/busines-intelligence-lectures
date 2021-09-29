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
Change DateTime to Date. 
    - TransformData. PowerQuery Manipualates Data without changing original data.
    - Select column "order_purchase_timestamp"
    - Right click and Transform
    - Select Date Only

# Reports with PowerBI
¿Cuántos clientes tenemos?. Podemos hacer esta consulta de acuerdo a un lapso de tiempo o histórico
customers_dataset -> customer_id

Answers 
¿Cuántas ventas tuvimos en 2017?
¿Comparativo de ventas 2017 y 2018?
Go to Models and see orders_dataset
    * orders_dataset->order_id
    * orders_dataset->order_purchase_timestamp
Filters

# Edición datos PowerQuery
- Transform Data Menu
- order_item_datasets (table)
- ¿Cuánto están pagando clientes por un producto?
- sum price and fright_value
- click on columns price and friht_value (shift to select both colums)
- Add column
- Standard / Add
-  change column labels: 
   -  Price
   -  Freight Cost
   -  Delivery Time
- change table name
  - Order Elements
