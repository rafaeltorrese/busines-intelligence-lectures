# Extending the Kimball Model

## Date dimensions and relationships

1. **Date dimensions and relationships.**
   Welcome back! Now, we'll cover creating date dimensions and defining relationships between tables.

2. **Date and time dimensions.**
   Date dimensions give us a built-in calendar which helps minimize complex date operations. For example, matching the company's fiscal year with the calendar year, or allowing users to slice by quarter or week. Time dimensions are similar to date dimensions but focus on time of the day. They are less common but can also be useful, particularly if your industry needs to track a time-of-day component.

3. **Options for creating a date dimension.**
   There are three common methods for creating a date dimension. The first is hosting a date dimension in the data warehouse. This allows you to easily update and share date dimensions with other services. However, this requires direct access to a database. Alternatively, you could store a date dimension in a text file. Power BI's support for text files is great, but the downside is that you'll need to create and update this text file manually. Thirdly, you can create a date dimension using DAX. This allows for full customization over what will be in the date dimension, and doesn't require external preparations. The downside is that you'll need to know how to write custom code, but once you've got the hang of it, this is a very powerful option.

4. **Creating a simple date dimension with DAX.**
   The starting point for creating a date dimension with DAX is the CALENDAR() function, which creates a series of dates.

5. **Creating a simple date dimension with DAX.**
   In this example, CALENDAR() creates a range of all dates between January first, 1950, and today, in a field called [Date].

6. **Creating a simple date dimension with DAX.**
   Using SELECTCOLUMNS(), you define which columns you want to keep from the [Date] field, in this case, Month and Year.

7. **Creating a simple date dimension with DAX.**
   Finally, we use DISTINCT() to avoid duplicates. A proper date dimension can include other columns, but this is a good start.

8. **Defining relationships.**
   Date or other dimension tables need to be linked to other tables, which is achieved by creating a relationship. Relationships allow us to easily propagate filters across tables and allow for cross-table calculations. Power BI automatically guesses relationships based on column names, but you can customize relationships manually as well.

9. **Relationship keys.**
   Relationships are based on keys: a column or set of columns which make a row in a table unique. There are two major types of keys. A natural key exists in the dataset and uniquely identifies something, such as an email address. Often, we'll need a surrogate key: an artificial number which increases by one for each row in the dataset, usually some identity column. Since Power BI requires single column relationships, we need a workaround for this.

10. **Relationship keys.**
    Here is where composite keys come into play. These are concatenated text fields made up of more than one column. Typically, composite keys are a combination of natural keys, such as the combination of name and birth year.

11. **Cardinality.**
    A relationship can connect one or more rows between tables. This is defined in the so-called cardinality of the relationship, which is a measure of the relationship between rows in one table with respect to another table. The most common type of cardinality between a dimension and a fact table is a many-to-one or one-to-many relationship. Note that these are virtually the same, in that they connect one row from the dimension to one or more rows in the fact table, or vice versa, depending on the direction you're looking. In many data modeling tools, a one-to-many or many-to-one relationship is denoted with a "one" and "asterisk" mark.

12. **Cardinality.**
    Two other cardinality types exist as well: one-to-one and many-to-many relationships. They are less common and are outside the scope of this course.

13. Let's practice!
    Let's recap what you've learned about relationships.

### Exercise 01-01.

**Cardinality**

Cardinality is an important consideration when working with tables in Power BI. By understanding the cardinality of a given relationship, you will be able to form expectations about how you can aggregate and visualize the data. If you expect one row but actually have many, it could cause duplication of results on screen or incorrect aggregations.

**A relationship from a fact to a dimension is typically which of the following?**

- One-to-many
- Many-to-one \*
- One-to-one
- Many-to-many

## Date dimensions and relationships in Power BI
1. **Date dimensions and relationships in Power BI**.
In this demo, we'll create a year dimension, extend that dimension, and then merge columns together to allow a relationship to be created where one otherwise couldn't be. To create a year dimension, go to the data view and select New Table. This will allow you to create a new table using DAX expressions. You should be familiar with the basics of DAX from the Power BI intro course, but note that, in the real world, date dimensions are often defined using copied and pasted code snippets. I've copied a code snippet, and will paste it here. This DAX expression will create a table named Year. It starts with defining all dates between January 1950 and today. From this range, the CALENDAR function creates a Date field under the hood. Next, only the year is retrieved in a column named Year, using the SELECTCOLUMNS function. Finally, to get the distinct years only, all this is wrapped in a DISTINCT function. There we have it: a table named Year, with one column named Year, with every year from 1950 up to the present, which as of the time of recording is 2021. To extend this year dimension, for example to include the millennium of the year, right-click the table and select new column. The new column will be called Millennium. I'm going to take the year column and subtract out the modulo division of year over 1000. This will leave 1000 for all years before 2000, and will be 2000 from there on out. Let's go back to the data model. We have our fact table, business establishment by age, and three dimensions: establishment age code, geography and NAICS code. The Year table is also visible, but is not yet linked to our fact table. To do that, drag the Year field of the Year dimension table to the Year field of the fact table. By default, a one-to-many relationship is defined from the dimension to the fact table, indicated by this arrow which goes from one to the asterisk. Since each row of Year is unique in the Year dimension table, Year can act as a natural key, and a one-to-many relationship is the correct choice here. When you don't have a unique key present in a table, you can create a composite key by merging multiple columns together. Suppose we didn't have this fact table with a unique key for NAICS Code, but this fact table instead, where the NAICS Code has been split up into four columns. As a result, there is no single field in this table that could have a relationship with the NAICS Code dimension table. Let's fix that by merging together the four columns. Right click the table to edit the query. Select Economic Sector, Subsector, Industry Group and Code by control clicking each one, and then right click to choose Merge Columns. In this case, I don't choose a separator, and I'll call the new column NAICS Code. With the NAICS Code created, close and apply the query. Power Query will automatically create a relationship between this fact table and the NAICS Code dimension, since there is now a unique identifier column in each of these tables. You can edit this relationship by double clicking it. Power BI automatically recognized that NAICS Code from the fact table relates with the 2017 NAICS code column, even when these columns don't have the same name. You can see here that Power BI assumed the cardinality as many-to-one. This seems correct, as there are many records in the fact table per row in NAICS Code. Perfect! Let's do some exercises.


1. **Date dimensions and relationships in Power BI.**
   In this demo, we'll create a year dimension, extend that dimension, and then merge columns together to allow a relationship to be created where one otherwise couldn't be. To create a year dimension, go to the data view and select New Table. This will allow you to create a new table using DAX expressions. You should be familiar with the basics of DAX from the Power BI intro course, but note that, in the real world, date dimensions are often defined using copied and pasted code snippets. I've copied a code snippet, and will paste it here. This DAX expression will create a table named Year. It starts with defining all dates between January 1950 and today. From this range, the CALENDAR function creates a Date field under the hood. Next, only the year is retrieved in a column named Year, using the SELECTCOLUMNS function. Finally, to get the distinct years only, all this is wrapped in a DISTINCT function. There we have it: a table named Year, with one column named Year, with every year from 1950 up to the present, which as of the time of recording is 2021. To extend this year dimension, for example to include the millennium of the year, right-click the table and select new column. The new column will be called Millennium. I'm going to take the year column and subtract out the modulo division of year over 1000. This will leave 1000 for all years before 2000, and will be 2000 from there on out. Let's go back to the data model. We have our fact table, business establishment by age, and three dimensions: establishment age code, geography and NAICS code. The Year table is also visible, but is not yet linked to our fact table. To do that, drag the Year field of the Year dimension table to the Year field of the fact table. By default, a one-to-many relationship is defined from the dimension to the fact table, indicated by this arrow which goes from one to the asterisk. Since each row of Year is unique in the Year dimension table, Year can act as a natural key, and a one-to-many relationship is the correct choice here. When you don't have a unique key present in a table, you can create a composite key by merging multiple columns together. Suppose we didn't have this fact table with a unique key for NAICS Code, but this fact table instead, where the NAICS Code has been split up into four columns. As a result, there is no single field in this table that could have a relationship with the NAICS Code dimension table. Let's fix that by merging together the four columns. Right click the table to edit the query. Select Economic Sector, Subsector, Industry Group and Code by control clicking each one, and then right click to choose Merge Columns. In this case, I don't choose a separator, and I'll call the new column NAICS Code. With the NAICS Code created, close and apply the query. Power Query will automatically create a relationship between this fact table and the NAICS Code dimension, since there is now a unique identifier column in each of these tables. You can edit this relationship by double clicking it. Power BI automatically recognized that NAICS Code from the fact table relates with the 2017 NAICS code column, even when these columns don't have the same name. You can see here that Power BI assumed the cardinality as many-to-one. This seems correct, as there are many records in the fact table per row in NAICS Code. Perfect! Let's do some exercises.

2. Let's practice!

### Exercise 02-01.

**Create a year dimension**

Time intelligence is a critical part of any business analysis, to the point where Power BI has several built-in features for creating date and time dimensions. Here, you will learn one easy technique for creating a year dimension using DAX.

1. Open `3_1_create_year_dimension.pbix`. from the Exercises folder on the Desktop.
2. Navigate to the _Data_ view and create a new table called `Year`.
3. Complete the following DAX syntax to create the `Year` table, which should contain a single column `Year`, with years ranging from 1961 to today's year.

```
____ = // name of the table
DISTINCT ( // only keeps unique rows
    SELECTCOLUMNS ( // returns a table and creates new column based on expression
        ____ ( DATE ( ____ ), ____ ), // creates date range between 1961-01-01 and today
        "____", YEAR([____]) // creates "Year" column, extracting the years only
    )
)

```

4.  - Navigate to the _Model_ view.
    - Use the Manage relationships feature to add a relationship between `Year` of `Business Establishment by Age` and the newly created `Year` dimension.
    - Make sure that the cardinality is such that many rows in `Business Establishment by Age` may correspond with one value in `Year`.

5.  - Navigate to the _Report_ view.
    - Add a _Card_ visual, with _Fields_ set to `Number of firms` from the `Business Establishment by Age` table.
    - Add a `Year` filter (from the `Year` dimension) and set to 1983 only.

6.  **How many manufacturing firms were there in 1983, according to the dataset? Answer in the form of ###K, where K represents thousands.** 597k

### Exercise 02-02.

**Extend the year dimension.**

The power of a date or time dimension is that you can extend the dimension by performing calculations one time instead of each time you query the data. For example, you might generate a date dimension which includes holiday information or information specific to your organization, such as fiscal year details or important company dates. In this exercise, you'll learn how to extract and use the decade from the `Year` dimension.

#### Instructions

1. In the _Data_ view, add a new column called `Decade` in the `Year` table, with the formula `'Year'[Year] - MOD('Year'[Year], 10)`
2. - In the _Report_ view, add a _Clustered column chart_ visual to the `Business Establishments` page.
   - The Values should be the maximum of `Number of firms` from the `Business Establishment by Age` table.
   - The _Axis_ should be `Decade` from the `Year` table.
3. **What was the maximum amount of firms during the 1980s?**

### Exercise 02-03.

**Composite key relationships**

When pulling data from multiple sources, it may be necessary to merge columns to connect datasets together by using a composite key. This is a vital skill, since Power BI requires single-column relationships between tables.

It seems that the database you usually extract data from has stopped providing you a geographic id in the tables. As a result, there isn't a single column you can use to create a relationship. While you wait for a fix from the data engineers, flex your column merging skills and create your own geographic key!

#### Instructions

1. Open `Summary Statistics for Manufacturing.txt` in Power Query.
2. <ul>
   <li>Change the data type for <code>Geography Summary</code> and <code>GeographyVariant</code> to "Text". </li>
   <li>Select <code>Geography Summary</code>, <code>GeographyVariant</code>, and <code>GeographyNation</code> (in this order) and merge the columns. </li>
   <li>Make sure that you keep the separator as ""--None--"". Call the new column <code>GEO_ID</code>.</li>
   </ul>
3. <div class=""><p>Select <em>Close &amp; Apply</em> to exit Power Query. Navigate to the <em>Model</em> view and review the relationships of the schema. Note that there are two fact tables now: one with <code>id</code> present in the raw data, one where you created a <code>GEO_ID</code> key yourself.</p>
   <p><em>If for some reason a new table is not showing up in the Model view, you can manually add a relationship using the Manage relationships icon in the Home menu. Click "New…" and select the tables and columns where you want to define the relationship.</em></p></div>

4. <div class=""><p>Add a relationship between the <code>Geography</code> dimension using the <code>id</code> column and the <code>Summary Statistics for Manufacturing</code> fact table.</p></div>

5. **What cardinality did Power BI set between the 'Geography' dimension and the 'Summary Statistics for Manufacturing' table?**
   - One-to-many *
   - Many-to-one
   - Many-to-one

## Granularity, measures, and hierarchies


1. **Granularity, measures, and hierarchies**.
   Let's talk about granularity, measures, and hierarchies.

2. **Understanding granularity.**
   Granularity refers to the level at which data is stored with respect to dimensions. This is the minimum level of detail we can query--we can aggregate data to higher levels, but won't be able to break it down to lower levels. You can get a good understanding of the grain of data by listening for the word "by" when describing a table. You might define a table by customer, by product, by day, so the granularity is that each row represents the combination of one customer, one product, and one day. In the example here, the granularity is by ID, by NAICS code, by establishment age, by year. Note that fields like number of firms are not counted as part of the grain: number of firms are measured based on the combination of dimensions.

NAICS: North American Industry Classification System 

3. **Handling granularity in Power BI**
If you have data at the annual level for example, there's no great way to break that data down by day. In some circumstances, you might use an allocation rule to spread values across the individual days, but those are estimations and introduce known inaccuracy to your data. By contrast, going from a finer grain to a coarser grain is easy to do with Power BI, by aggregating and grouping. In Power BI, you can specify aggregations and how to summarize data. Grouping is the more detailed process, allowing you to specify the grouping of columns as well as specific aggregations. Both methods have two key benefits. First, with fewer rows, we can get better query performance when displaying visuals. Second, by storing fewer rows, we reduce the amount of memory needed to store this data which can improve refresh time.

4. **Measures.**
   Measures are fields, or combinations of fields, which can be aggregated or calculated. They make up the majority of fields in fact tables. Measures can be gathered directly from the raw, imported data, such as the fields from this fact table. They can be aggregated using sum, average, or count for example. New measures can also be calculated from raw data to provide more insights.

5. **Creating measures.**
   When you bring a numeric value into Power BI, it is automatically aggregated using the sum. You can change the summarization to other aggregation methods, or use DAX. DAX is a powerful tool to create aggregations or new measures, and is covered in-depth in other Power BI courses, although we'll see some in this lesson. If you're new to DAX, Power BI has a dialog, called Quick measures, to let you create specific types of measures very easily. Most quick measures let you choose a calculation, base it on a value, and group the data by some other value. Each quick measure has its own template, which is great for learning how to create moderately complex measures.

6. **Hierarchies.**
   Lastly, let's talk about hierarchies. Hierarchies allow users to drill down into the data dimensions. There are two types of hierarchies. Natural hierarchies fit clearly in the real world. A classic example of this is in the date dimension: each year is made up of months, which are made up of days. Each level fits cleanly into the level above. By contrast, week is not part of this hierarchy, as a week may span across two months or two years. Artificial hierarchies exist only for the purpose of querying. For example, the intake year, favorite color, and favorite sport of students don't flow naturally from one another, but if users always drill down from intake year into favorite color and then favorite sport, this hierarchy makes sense.

7. **Let's practice!.**
   Let's test your knowledge on hierarchies before moving to Power BI.

### Exercise 03-01. Hidden hierarchies

Drag each hierarchical level to the correct natural hierarchy (Date or Product) that makes sense to the end user. The other attributes should go in the Neither bucket.

- Date hierarchy
  - Calendar quarter
  - Month
  - Year
- Product hierarchy
  - Product subcategory
  - Product name
- Neither hierarchy
  - Number of products
  - Product color
  - Week

## Hierarchies and measures in Power BI

1. **Hierarchies and measures in Power BI**.
   To create a hierarchy in Power BI, go to the data view. In this example, Century will be the highest level of the Year hierarchy. Right click on the dimension you want to create a hierarchy on, and select Create hierarchy. You can rename the hierarchy by double clicking it. There is also a Decade field, which can be added to the hierarchy by right clicking, and then select Add to hierarchy. The same thing applies to the Year field. It is entirely optional, but as best practice, it's a good idea to hide the other columns. Changing the granularity of the data by aggregating measures happens in Power Query. Let's say for example that you only need the sum of firms and employees per year, but that the raw data takes too long to load. You can then aggregate these measures in Power Query, which will speed up the process. First, let's duplicate Business Establishment by Age. In the Transform menu, select Group by, and click Advanced for better control of the aggregations. The grouping will be per year, which you set on top, and the aggregations for this example are the sum of the number of firms, and the sum of the number of employees. You can rename the new columns here as well. This will modify the query and only import the fields we just specified. Let's call the table Firms_Employees by Year, with every row containing the total number of firms and employees per year. Creating new measures in Power BI is mostly handled by using DAX. Let's for example create a new measure called Employees per Firm. You can use the DIVIDE function to divide the sum of employees by the sum of firms. The DIVIDE function has the advantage of not throwing an error when the denominator is zero. Note that this new calculated measure won't show up in this table, as it is only run when you use it in a visualization. The last thing to demonstrate, is the use of Quick measures. Quick measures give the ability to generate some moderately complex DAX, based on an interactive template. For example, let's calculate a running total of the number of employees, per year. Select the calculation (Running total), the Base value (Sum of Employees), and the Field (Year). So, how does this look like in a report? Let's create a Matrix, with the Year hierarchy on the rows, so that you can drill down into Century, Decade, and Year. Add Employees, Firms, and Employees per Firm as the Values. By using these collapse buttons, or these drill down buttons, you can see the individual rows per year, or aggregated by a higher level in the hierarchy. The Running total can be visualized using a table, with the Year and Employees Running total column. You can see that there is a consistent increase over time until we get to our grand total of 1 point 3 billion employees. Up to you now!

2. **Let's practice!**.

### Exercise 04-01.

**Build a hierarchy**
Hierarchies allow business users to drill down into categorical data on Power BI visuals. It works extremely well in conjunction with visuals such as treemaps.

#### Instructions

1. <div class=""><p>Load <code>3_4_build_hierarchy.pbix</code> from the Exercises folder on the desktop.</p></div>
2. <ul>
   <li>In the <em>Data</em> view, create a hierarchy on <code>SUBSECTOR</code> in the <code>NAICS Code</code> dimension. </li>
   <li>Rename the hierarchy to <code>NAICS Code hierarchy</code>.</li>
   </ul>
3. <div class=""><p>Add on the following columns in this order to the hierarchy: <code>Industry group</code> and <code>2017 NAICS Code</code>.</p></div>
4. <div class=""><ul>
   <li>Navigate to the <em>Report</em> view and create a new page called <code>Summary Stats</code>. </li>
   <li>Add a new <em>Treemap</em> visual, with the values of <code>Number of employees</code> from the <code>Summary Statistics for Manufacturing</code> dataset split by the <code>NAICS Code hierarchy</code>.</li>
   </ul></div>
5. <div class=""><p>Add a <em>Slicer</em> for <code>Year</code> (from <code>Summary Statistics for Manufacturing</code>) and set to 2018.</p></div>
6. <div class=""><p>Enable "Drill down" on the treemap by selecting the down arrow marked "Click to turn on Drill down." Try and click on a category on the treemap to drill into.</p></div>
7. **How many employees were hired in manufacturing sector with 2017 NAICS Code "325510" in the year 2018?** 35569

### Exercise 04-02.

**Change the granularity of a query**

<div class=""><p>Power BI has excellent data aggregation capabilities, but often you want to pre-aggregate data in Power Query before exposing it to business users. For example, suppose you retrieve data from a system that tracks individual debits and credits from an accounting system: you could aggregate these individual operations up to the daily grain to make it easier to spot patterns and to keep files sizes smaller. In this exercise, you'll aggregate on the average amount of number of employees per year and per geographic ID.</p>
</div>

#### Instructions

1. <ul>
   <li>In Power Query, duplicate the <code>Business Establishment by Age</code> query. </li>
   <li>Rename it to <code>Establishments</code>.</li>
   </ul>
2. <div class=""><p>Select the <code>id</code> and <code>Year</code> columns and then open the <em>Group By</em> menu.</p></div>
3. <div class=""><p>In the "Group By" window, add a new column name: <code>AvgEmployees</code>, as the average of the <code>Number of employees</code>. Then close and apply the changes.</p></div>
4. <div class=""><ul>
   <li>In the <em>Report</em> view, create a new page called <code>Establishments</code>. </li>
   <li>Add a <em>Line chart</em> visual, of <code>AvgEmployees</code> by <code>Year</code> from the <code>Establishments</code> table.</li>
   </ul></div>
5. **In which year in this dataset did the smallest average number of employees in the manufacturing sector occur?**
   - 2009
   - 2010 *
   - 2011

### Exercise 04-03.

**Measures and quick measures**

<div class=""><p>Sometimes your dataset will include all of the measures you need for analysis. Quite often, however, you will need or want to create your own measures in order to make data analysis easier for business users. In this exercise, you're asked to investigate how the number of employees per firm and by age of establishment changed over time. You're going to create your own measures, both manually through DAX, as well as using quick measures, to answer the last two questions of this chapter.</p>
<p><em>If you have lost any progress, close any open reports and load <code>3_6_measures.pbix</code> from the Exercises folder on the desktop.</em></p></div>

#### Instructions

1. <div class=""><p>In the <code>Business Establishment by Age</code> table, create a new measure called <code>Employees per Firm</code>, as the sum of <code>Number of employees</code> divided by the sum of <code>Number of firms</code>.</p></div>
2. <div class=""><ul>
   <li>Create a quick measure. </li>
   <li>Use <code>Average per category</code> as the <em>Calculation</em>, the sum of <code>Number of employees</code> from <code>Business Establishment by Age</code> as the <em>Base value</em>, and <code>Establishment age code</code> from <code>Establishment Age Code</code> as the <em>Category</em>. </li>
   <li>Call this new measure <code>Average Number of Employees by Age</code>.</li>
   </ul></div>
3. <div class=""><ul>
   <li>Create a new page called <code>Jobs</code>. </li>
   <li>Add a <em>Table</em> visual, with the following columns: <code>Geographic Area Name</code>, <code>Year</code>, <code>Employees per Firm</code>, and <code>Average Number of Employees by Age</code> from the <code>Business Establishment by Age</code> table.</li>
   </ul></div>
4. Which state had the single smallest number of employees per firm in the dataset, over all years? Montana What was the average number of employees by age for that state and year? 2470
