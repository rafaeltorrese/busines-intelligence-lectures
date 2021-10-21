# Section 02. Modeling Data

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