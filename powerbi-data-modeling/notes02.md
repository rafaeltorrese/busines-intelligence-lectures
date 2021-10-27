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
    + `Quantity Ordered`  (whole number)
    + `Order Amount`  (decimal number)
    + `Order Date`  (date)
- Dimension
    + `Item Description`  (string)
    + `Shipping ZIP Code`  (string)
    + `Customer Date of Birth`  (date)
    + `Customer Joined Date`  (date)
  
## Lesson01. Star Schema. Instructor

### Transcript


Got It!
1. Creating a star schema
Hey there, welcome back. Let’s take a look at how we can actually implement a simple star schema in Power BI! In this demo, we’ll take a data file and break it out into a fact and a dimension table. We’ll also load a separate file as a new dimension. The first thing we’ll do is go to the data menu and then select text/CSV to load a CSV file. I'm going to choose the Establishment Survey dataset. I will select Transform Data to open Power Query. Let’s take a look at the data first before making any changes. As you can see, we have data about the geography of the establishments, both at the country and at the state level. It seems like we also have some information about the establishment size. However, this is just the id, we don’t know what the actual meaning of those values are yet. Lastly, we know the year the data was gathered, and the number of establishments is the measure that will go in our fact table. Let’s split this file into a fact table and a geography dimension. I’ll start by duplicating the query. This new query will form our dimension table. I’m going to rename it to Geography. We only want to keep the columns that provide more information about the geography. So I’ll keep Country id, Country, State id, and State. I’ll select them by holding the shift key and then I can keep only these columns by right-clicking and selecting Remove Other Columns. Now I want to reduce duplicates, to ensure we store the data in the most efficient way. To do that, I’ll right click again and click Remove Duplicates. Now every row in the Geography table is unique. Let’s go back to the fact table. Since the geography information is stored in our new dimension, it’s not necessary to keep it here as well. Except for the id. This is because we’ll need to be able to connect the dimension to the fact. So we’ll keep the State id as a key in the fact table and remove the rest. There we go. Our fact table is done. I’ll close and apply the changes made. In the data view, we can see both tables now. The last thing I’m going to do is add a Size dimension. As you can see we have a size id in the fact table, but we don’t know what the ids stand for. Let’s fix that by loading another file. I’ll click Get data and select the Establishment Size dataset. As you can see, this file contains the actual meaning of the size id, which is exactly what we need. I’ll go to Power Query again and I’m going to rename the table to Size. As you can see there are a lot of duplicate values, so let’s remove those. That looks better. Let’s close and apply and go take a look at the data model. To get a better view of the data model, you can collapse the Properties and Fields panes on the right. There is also a slider to zoom in and out of the Data View on the bottom right of Power BI. Here we can see the fact table and the two dimensions. The only thing left to do is to make sure there is a relationship between the fact table and the Size dimension. Size is connected to Establishment Survey by the Size Id. That’s it! Using this star schema, we can start creating reports to get insights about the establishments, sliced by geography and establishment size. Your turn!

2. Let's practice!


1. The first thing we’ll do is go to the data menu and then select text/CSV to load a CSV file. I'm going to choose the Establishment Survey dataset.
2. Transform Data to Open Power Query
3. we have data about the geography of the establishments, both at the country and at the state level
4. It seems like we also have some information about the establishment size. However, this is just the id, we don’t know what the actual meaning of those values are yet.
5. we know the year the data was gathered, and the number of establishments is the measure that will go in our fact table
6. Let’s split this file into a fact table and a geography dimension. 
7. I’ll start by duplicating the query. 
8. This new query will form our dimension table. 
9. I’m going to rename it to Geography
10. I’ll keep Country id, Country, State id, and State.
11. Now I want to reduce duplicates, to ensure we store the data in the most efficient way
12. Let’s go back to the fact table. Since the geography information is stored in our new dimension it’s not necessary to keep it here as well. Except for the id.
13. . So we’ll keep the State id as a key in the fact table and remove the rest. There we go. Our fact table is done. I’ll close and apply the changes made.
14. The last thing I’m going to do is add a Size dimension. As you can see we have a size id in the fact table, but we don’t know what the ids stand for. Let’s fix that by loading another file. 
15. Get data and select the Establishment Size dataset
16. I’ll go to Power Query again and I’m going to rename the table to Size.

### Exercise 01-01

Food Manufacturing

### Exercise 01-02

**Load a new dimension**

Sometimes, you'll want to import a separate file as a dimension. This will further extend the amount of relevant information you can learn given your fact data. In our case, it would be nice to have some more time-related information. Adding a **Time**  dimension will allow us to aggregate data not just at the year-level, but also the decade- or even century-level. Let's continue with the star schema from before:

1. Import the file named `Time.txt`  from the `dataset02`  folder in the `datasets`  directory.
2. Go to the _Model_  view and verify that there is a relationship between the "Time" dimension and the fact table defined by the `Year`  column.
3. Return to the _Report_  view and add a new slicer visual, slicing on `Decade`  from the Time dimension.
4. Change the slicer to be a list of values rather than a range.
5. **How many employees did the Food Manufacturing subsector count on average during the 90s?** 3164002.59

### Exercise 01-03

**Create another dimension**
Time to add the final dimension, **Age** . In the data you can see that we have information about the `Age code`  for each establishment, but we don't know what the actual meaning of those values is. Let's load another file as a new dimension to allow for slicing by establishment age.

1. Import the file named `EstablishmentAge.csv`  from the `dataset02`  folder in the datasets  directory.
2. Go to Power Query and name the table "Age".
3. Remove duplicate values from the dataset and then close Power Query.
4. Navigate to the _Model_  view and connect the Age dimension to the Establishment Survey fact by `Age code`  if this is not the case yet. _If for some reason a new table is not showing up in the Model view, you can manually add a relationship using the Manage relationships icon in the Home menu. Click "New…" and select the tables and columns where you want to define the relationship._
5. Return to the _Report_  view and add a slicer on `Establishment Age`  from the new Age dimension.
6. **How many average employees did 3-year old firms in the Food Manufacturing subsector have during the 90s?**