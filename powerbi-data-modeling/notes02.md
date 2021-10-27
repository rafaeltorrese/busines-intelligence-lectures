# Section 02. Modeling Data

1. Dimensional modeling
   Welcome back! I'm Sara and I will be your instructor for this next chapter. Earlier, you learned that data models provide a conceptual representation of data elements and the relationships between them. There are many approaches to data modeling. We'll focus on one, the dimensional model.

2. The Kimball Model
   The Kimball model, otherwise known as the dimensional model, is one of the most popular approaches to data modeling.

3. The Kimball Model
   There are two key concepts in the Kimball model: facts and dimensions. Facts are the metrics from your business process. Dimensions provide the context surrounding a business process. These combine to form a star schema. The star schema's name comes from the way that facts and dimensions connect. We typically have several dimensions surrounding each fact. In this example, measures related to Property Sales are stored in the fact table, and the Lender, Salesperson, Date, Property, and Payment Type tables provide more context about each property sale. Huge amounts of data are organized in this way in data warehouses. Power BI is optimized to use star schemas over any other way of loading data, so Power BI is faster and easier to use with a dimensional approach.

4. Fact tables
   Let's take a closer look at fact tables first. A fact table typically has two types of columns; facts and keys. Facts are the measures or metrics from your business process. Examples include sales, employee count, or number of website visits. They are generally dates and numbers which we can aggregate in some way. Keys are how we establish relationships between fact tables and dimension tables. We expect fact tables to be tall and narrow. They have lots of rows, so we try to minimize the number of columns and how big those columns are.

5. Fact tables: an example
   Here is an example of a fact table, Property Sales. Each row represents a property that was rented at a specific date.

6. Fact tables: an example
   The first five columns contain keys or IDs that are used to link to each of the dimension tables. You'll find more information about the lender, date, property, payment type, and salesperson there.

7. Fact tables: an example
   The last two columns hold the measures. Here we're tracking the rent, in dollars, and the duration of the rental agreement, in months.

8. Dimension tables
   Next, we'll look at dimension tables which provide the context around facts. A fact may tell you how much or how often, but dimensions give the rest of the story. Who did it, how they did it, where they did it, and so on. Dimensions are shared business concepts, usually in the form of a noun such as Person, Employee, Customer, and Vendor. Dimensions contain static or slowly-changing data. Think of information like names, dates of birth, and height. Dimension tables are typically short and wide. They don't contain that many rows, but do contain a large amount of context for the facts.

9. Dimension tables: an example
   Let's take a look at an example. Here you can see the Salesperson table.

10. Dimension tables: an example
    The first column contains the same key as in the fact table and can be used to combine the information from both tables.

11. Dimension tables: an example
    The table also stores additional attributes about each salesperson in the company.

12. Star schema
    Here's that same star schema from before. In the Kimball model, dimensions are often used in multiple facts. These dimensions surrounding Property Sales could provide context to a different fact table as well. In a star schema, dimensions do not link to other dimensions.

13. The dataset
    This chapter will continue with the Census data about establishments active in the manufacturing sector. In the exercises, you will be creating a fact table that contains measures like number of employees, number of firms, and so on. Additionally, there will be more information about the establishment in the form of dimension tables. These include data on the industry, time, age, and geography of the establishments.

14. Let's practice!
    Let's check your understanding of dimensional modeling!

## Exercise 01

- Fact
  - `Quantity Ordered` (whole number)
  - `Order Amount` (decimal number)
  - `Order Date` (date)
- Dimension
  - `Item Description` (string)
  - `Shipping ZIP Code` (string)
  - `Customer Date of Birth` (date)
  - `Customer Joined Date` (date)

## Lesson02. Star Schema. Instructor

### Transcript

Got It!

1. Creating a star schema
   Hey there, welcome back. Let’s take a look at how we can actually implement a simple star schema in Power BI! In this demo, we’ll take a data file and break it out into a fact and a dimension table. We’ll also load a separate file as a new dimension. The first thing we’ll do is go to the data menu and then select text/CSV to load a CSV file. I'm going to choose the Establishment Survey dataset. I will select Transform Data to open Power Query. Let’s take a look at the data first before making any changes. As you can see, we have data about the geography of the establishments, both at the country and at the state level. It seems like we also have some information about the establishment size. However, this is just the id, we don’t know what the actual meaning of those values are yet. Lastly, we know the year the data was gathered, and the number of establishments is the measure that will go in our fact table. Let’s split this file into a fact table and a geography dimension. I’ll start by duplicating the query. This new query will form our dimension table. I’m going to rename it to Geography. We only want to keep the columns that provide more information about the geography. So I’ll keep Country id, Country, State id, and State. I’ll select them by holding the shift key and then I can keep only these columns by right-clicking and selecting Remove Other Columns. Now I want to reduce duplicates, to ensure we store the data in the most efficient way. To do that, I’ll right click again and click Remove Duplicates. Now every row in the Geography table is unique. Let’s go back to the fact table. Since the geography information is stored in our new dimension, it’s not necessary to keep it here as well. Except for the id. This is because we’ll need to be able to connect the dimension to the fact. So we’ll keep the State id as a key in the fact table and remove the rest. There we go. Our fact table is done. I’ll close and apply the changes made. In the data view, we can see both tables now. The last thing I’m going to do is add a Size dimension. As you can see we have a size id in the fact table, but we don’t know what the ids stand for. Let’s fix that by loading another file. I’ll click Get data and select the Establishment Size dataset. As you can see, this file contains the actual meaning of the size id, which is exactly what we need. I’ll go to Power Query again and I’m going to rename the table to Size. As you can see there are a lot of duplicate values, so let’s remove those. That looks better. Let’s close and apply and go take a look at the data model. To get a better view of the data model, you can collapse the Properties and Fields panes on the right. There is also a slider to zoom in and out of the Data View on the bottom right of Power BI. Here we can see the fact table and the two dimensions. The only thing left to do is to make sure there is a relationship between the fact table and the Size dimension. Size is connected to Establishment Survey by the Size Id. That’s it! Using this star schema, we can start creating reports to get insights about the establishments, sliced by geography and establishment size. Your turn!

2. Let's practice!

3. The first thing we’ll do is go to the data menu and then select text/CSV to load a CSV file. I'm going to choose the Establishment Survey dataset.
4. Transform Data to Open Power Query
5. we have data about the geography of the establishments, both at the country and at the state level
6. It seems like we also have some information about the establishment size. However, this is just the id, we don’t know what the actual meaning of those values are yet.
7. we know the year the data was gathered, and the number of establishments is the measure that will go in our fact table
8. Let’s split this file into a fact table and a geography dimension.
9. I’ll start by duplicating the query.
10. This new query will form our dimension table.
11. I’m going to rename it to Geography
12. I’ll keep Country id, Country, State id, and State.
13. Now I want to reduce duplicates, to ensure we store the data in the most efficient way
14. Let’s go back to the fact table. Since the geography information is stored in our new dimension it’s not necessary to keep it here as well. Except for the id.
15. . So we’ll keep the State id as a key in the fact table and remove the rest. There we go. Our fact table is done. I’ll close and apply the changes made.
16. The last thing I’m going to do is add a Size dimension. As you can see we have a size id in the fact table, but we don’t know what the ids stand for. Let’s fix that by loading another file.
17. Get data and select the Establishment Size dataset
18. I’ll go to Power Query again and I’m going to rename the table to Size.

### Exercise 02-01

**Splitting data into facts and dimensions**

Datasets will frequently come in a "wide" format, containing both fact and dimensional data. Breaking these files out into facts and dimensions will improve queries and can improve performance on larger datasets. In the next few exercises, we'll be creating the following star schema:

![Star Schema](ex_screenshot_01-02.png "Star Schema")

1. Load the file `Establishment Survey.csv`
2. Duplicate the Business "Establishment Survey" query and rename it to "Industry".
3. Keep only the following columns in the "Industry" table: `NAICS code`, `NAICS Code Description`, `Industry group code`, `Industry group`, `Subsector Code`, `Subsector`, `Sector Code`, and, `Sector`. Remove duplicate values from the dataset.
4. Return to the "Establishment Survey" query and remove the columns you just added to "Industry": `NAICS Code Description`, `Industry group code`, `Industry group`, `Subsector Code`, `Subsector`, `Sector Code`, and, `Sector`. Make sure to keep `NAICS code` ! This column is the key we'll use to connect the dimension to the fact table. Exit _Power Query_
5. Go to the _Model_ view to verify that there is a relationship between "Industry" and "Establishment Survey". _If for some reason a new table is not showing up in the Model view, you can manually add a relationship using the Manage relationships icon in the Home menu. Click "New…" and select the tables and columns where you want to define the relationship._
6. Go to the _Report_ view and create a new clustered bar chart visual with the `Subsector` column from the dimension table as the Axis and **Average** `Number of employees` from the fact table as the _Values_.
7. **Which subsector counted the highest average number of employees?** Food Manufacturing

### Exercise 02-02

**Load a new dimension**

Sometimes, you'll want to import a separate file as a dimension. This will further extend the amount of relevant information you can learn given your fact data. In our case, it would be nice to have some more time-related information. Adding a **Time** dimension will allow us to aggregate data not just at the year-level, but also the decade- or even century-level. Let's continue with the star schema from before:

1. Import the file named `Time.txt` from the `dataset02` folder in the `datasets` directory.
2. Go to the _Model_ view and verify that there is a relationship between the "Time" dimension and the fact table defined by the `Year` column.
3. Return to the _Report_ view and add a new slicer visual, slicing on `Decade` from the Time dimension.
4. Change the slicer to be a list of values rather than a range.
5. **How many employees did the Food Manufacturing subsector count on average during the 90s?** 3164002.59

### Exercise 02-03

**Create another dimension**
Time to add the final dimension, **Age** . In the data you can see that we have information about the `Age code` for each establishment, but we don't know what the actual meaning of those values is. Let's load another file as a new dimension to allow for slicing by establishment age.

1. Import the file named `EstablishmentAge.csv` from the `dataset02` folder in the datasets directory.
2. Go to Power Query and name the table "Age".
3. Remove duplicate values from the dataset and then close Power Query.
4. Navigate to the _Model_ view and connect the Age dimension to the Establishment Survey fact by `Age code` if this is not the case yet. _If for some reason a new table is not showing up in the Model view, you can manually add a relationship using the Manage relationships icon in the Home menu. Click "New…" and select the tables and columns where you want to define the relationship._
5. Return to the _Report_ view and add a slicer on `Establishment Age` from the new Age dimension.
6. **How many average employees did 3-year old firms in the Food Manufacturing subsector have during the 90s?**

## Lesson03. Star and snowflake schemas. Instructor

1. Star and snowflake schemas
   Welcome back! Let's continue building on your knowledge from earlier. In this video, we'll take a look at snowflake schemas, an extension of the star schema.

2. Star schema
   Remember from earlier that a star schema consists of one or more fact tables surrounded by dimension tables.

3. Snowflake schema
   The snowflake schema is like a star schema, except it allows relationships between dimensions. In the example you can see that the Lender and Property dimensions each link to other dimension tables. Note that fact tables remain the same.

4. A closer look
   The biggest difference between the two styles is how they handle hierarchical data. Star dimensions tend to have all levels of a hierarchy in the same table, whereas with snowflake dimensions, hierarchy levels are explicitly broken out into multiple tables. Here you can see a Product dimension table. Imagine that each product has a name. Each product also belongs to a product subcategory, which itself belongs to a product category. In a star schema, all levels of the hierarchy, as well as their attributes, show up on the same product dimension. With a snowflake schema, each level of the hierarchy becomes its own table and we join those tables, usually with keys.

5. Comparison
   When it comes to dimensional modeling theory, we strongly prefer star schemas over snowflake schemas. The key reason is that star schemas are easier for business users to understand. They don't want to worry about keys or hierarchies. The other benefit is that quite a few business intelligence tools have been optimized for the star schemas. Although dimensional modeling theory leans heavily toward star schemas, we do see snowflake schemas in some data warehouses. The reason for this is that star schemas duplicate quite a bit of data, which leads to storage costs and can impact performance. Also, star schemas are not ideal for frequently-updated data, especially with large dimensions. Suppose you have millions of rows in a dimension containing a column for country. When a country name changes, you may have to update a large number of rows with the new country name. By contrast, with a snowflake schema this would be an update of a single row.

6. Stars and snowflakes in Power BI
   When it comes to Power BI in particular, it is important to note that both schemas work. If you have a snowflake schema in an existing warehouse, you could import the data as-is, making migrations easier. That said, Power BI does prefer star schemas for the same reason as dimensional modeling theory. Because it is easier for users to understand. Furthermore, there are some optimizations in Power BI which make performance much less of a concern.

7. The performance analyzer
   Power BI has a built-in performance analyzer. When enabled, it keeps track of at least three key measures on each visual. The first is how long it took to read the data from its internal database and then perform any DAX operations on the data. The second component is figuring out how long it took the visual to render. Finally, a third measure captures everything else, which is typically waiting time on other operations, including waiting for cross-filtering operations to complete.

8. Performance tuning advice
   There are a number of ways you can improve performance. If the DAX query takes a long time to complete, you could tune your DAX operations or improve your data loading performance. This might include improving your data model! If the big problem is in visual display, use less complicated visuals and show less information on the screen. Power BI needs to render each data point, so plotting tens of thousands of points may take a while. If the Other value is the cause of your slowness, you might want to reduce the number of visuals on the page.

9. Let's practice!
   Time to practice!

### Exercise 03-01

## Lesson04. Evaluating performance. Instructor

1. Evaluating performance
   In this demo, we’ll see how to create a snowflake schema and learn how to use the performance analyzer. Here in the model view, you can see the star schema I created earlier. If we take a closer look at the Geography dimension, we can see that it is made up of hierarchical data. Country first, then State. One of the main differences between star and snowflake schemas is how they handle hierarchical data. Since in the snowflake schema dimensions can be connected to other dimensions, we can split out the state and country information. Let’s do exactly that! I’ll go into Power Query by clicking Transform data. I’ll duplicate the geography table twice and rename the new tables Country and State. Let’s think about how we want to connect to the fact table. The most detailed level of geography is State, and that is also the id that is present in the fact table. So we’ll connect the State table to Establishment Survey. We’ll also need to connect the State table to the Country table, which means we need to keep the Country id as well. But the actual country value can be removed here. I’ll right-click and select Remove. Next, we’ll look at the Country table. This one should contain only country information, so I’ll remove all state data. Let’s also remove the duplicate rows. Looks like there is only one country in our data at the moment. Note that if the country value would have to be updated, we only have to do it in one place in this snowflake schema, whereas it would be a lot more cumbersome to do this in the star schema from before. Let’s close and apply and take a look at the data model. Note that I’ve kept the Geography star dimension as well, so we can easily compare performance later on. In a real-life situation, you would use only one of the two approaches. You can see that Power BI has automatically created relationships between the star dimension and the snowflake dimensions. This is not right. Let’s remove them. I’ll right click on the line and select Delete. Let’s do the same for the other table. There we go! So these are our snowflake dimensions. Now I’m going to create a relationship between the fact and State tables. I could drag the column names on top of eachother or use the Manage relationships button here. I’ll select New and choose the two tables. You can see that Power BI has recognized State id as the key, which is correct. Click OK and close. Lastly, you can see that the relationship between State and Country is a dotted line, which means it’s inactive. Let’s quickly change that by going into Properties. There we go. That’s our snowflake schema. And this would be our star schema. I’m going to go into the Report view and create two visualizations. First, I’ll create a bar chart with the number of establishments by state, using the field from the star dimension. Then, I’ll do the same but use the snowflake dimension for the state. Let’s quickly rename these visuals to star schema and snowflake schema. Now, we can compare the performance. I’ll go to View here at the top and click on Performance analyzer. This pops out the Performance analyzer pane. I’ll start recording and then refresh the visuals. This will show me the time it takes to load the two visuals on the page in milliseconds. If I refresh a couple of times, we can see that one schema isn’t consistently faster than the other. With our small dataset everything loads pretty quickly, but if you’re working with thousands or millions of rows, the star schema should be more efficient. This is because star schemas will only join the fact table with the dimension tables, leading to faster execution times. That’s it, time for some exercises!

2. Let's practice!

### Exercise 04-01

### Exercise 04-02

### Exercise 04-03
