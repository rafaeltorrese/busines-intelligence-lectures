# Section 01. Defining Tables

Got It!
1. Data modeling and table properties
Welcome! My name is Maarten, and I'll be one of your instructors in this course on modeling data in Power BI.

2. What is a data model?
So, what is a data model? In short, a data model is a conceptual view of data elements. Typically, this is done in the form of a diagram. Data models include tables, columns, and relationships between tables. They can also include information on data types and keys.

3. Data modeling
Data modeling is the process of creating a data model. It's a critical part of Power BI development. Incoming data usually needs some cleanup and often substantial alterations to the data to find the right insights. This includes changing columns to join together disparate tables, removing non-data rows, or comprehensive changes like pivoting tables. As a result, data modeling techniques can shrink down the amount of disk space needed to store and process data, which improve speed. Finally, data modeling makes the model easier for business users to interpret.

4. Data modeling in Power BI & Power Query
Data modeling in Power BI is mainly handled by Power Query, the query editor for Power BI and other Microsoft products, like Excel. Its main purpose is to manage the queries which drive dashboards and reports, but also to assist with data modeling. Power Query directly changes the data, such as removing columns. You define your base changes in Power Query, and perform fine-tuning steps in Power BI.

5. Columns and row management
Let's overview some key data modeling steps you can do in Power Query and Power BI. On a column and row level, there are several options, such as removing specific columns, using the first row as the header, breaking out a lengthy column into multiple, independent columns, or summarizing data in a table and grouping it by another column.

6. Data types
In Power Query and Power BI, columns can be assigned to data types. The motivation is to constrain your data, ensuring that values match expectations. This can also optimize storage: the numeric value 1,000,000 fits in four bytes but would take nine bytes as a string. Some functionality is limited to specific types--for example, date arithmetic is only possible on date and time columns. Power Query usually correctly infers the data types of columns, and does so using the first few hundred rows.

7. Rounding
We could also specify decimal places in Power Query. This actually changes the loaded data, so it isn't just a formatting choice. This is useful when there are strict rounding rules. However, typically, we want to round after performing all calculations, so rounding in Power Query is uncommon. Formatting within Power BI itself changes the data's appearance but doesn't affect the stored data. Thus, rounding happens after any calculations. Therefore, we usually prefer rounding here than in Power Query. You now know a few key ways to alter data in Power BI, but these aren't the only ones. You'll discover more during the upcoming videos and exercises about string operations and other column modifications!

8. The dataset
The dataset we'll be using comes from the United States Census Bureau and summarizes survey data asked of manufacturing firms in 2018 and 2019. It contains a variety of measures around payroll and numbers of employees for several industries according to the North American Industry Classification System (or NAICS). In later exercises, we'll extend this dataset with geography, time, and other dimension tables.

## Lesson 01. Data Modeling And Table Properties
Welcome to the first demo. This course will focus on how to model your data in Power BI. Throughout the demos, you'll explore a toolbox of various techniques from which you can choose the right tools to model your data. Let's start with loading the NAICS manufacturing dataset. Select Get data and then choose Text/CSV. This csv contains several metrics of manufacturers per state per year. Selecting Transform Data brings you into Power Query. Here, you can see that there are two distinct rows on the top: one is a header with short names, one is a header that has descriptive labels. I want to keep this second row for my headers. To remove the first row, select Remove Rows and then Remove Top Rows. You are asked how many rows you want to remove, so enter "1" in this case. Now, you can take this new first row and use it as the headers. To do that, simply choose Use First Row as Headers. Note that this changed data types automatically: industry group for example is now considered an integer. If you need to change that back to text you click the data types icon, and select Text from the list of data types. You're asked whether you want to replace the current data type conversion, or if you want to add a new conversion step. Replacing it is the default option, since it minimizes the amount of data type conversion steps. Note that there is no default undo action in Power Query. If you want to undo a certain data transformation step at any point, you can do so by clicking the x mark next to a step in the list on the right. Now suppose that your users are used to seeing the Meaning of NAICS in all lowercase. You can change this in two ways: by right clicking the column, selecting Transform, or by going to the Transform menu at the top, and select Format. Either way allows you to transform this column into lowercase. With text transforms, you can also for example add a prefix to the industry group. This can only be done in the Transform menu. Choose Format, and then Add Prefix. Doing this allows you to put in some hard coded value before each value in the industry group. In this example, you can see "Code: ", followed by the original number. You can also perform some arithmetics on your numerical values. Open the right-click menu or select Scientific in the Transform menu to see the different options. Since there are quite a few orders of magnitude between values, you could choose to transform your data using the natural logarithm, for example. Double click the header to change the name of the column accordingly. Note that we also could round the numbers here in Power Query, but this would actually remove the number of decimals during the data load, rather than hiding them. To apply all your changes and return to Power BI, click Home and then Close & Apply. This will load your data and perform all the steps we just defined. OK, let's look at some operations you could perform in Power BI. Go to the Data view, and select a column to reveal the Column tools menu. In here, you have different options that only alter the visual representation of the data, like changing the formatting, currency, rounding, or data category. Recall that Subsector was a numeric column, but it doesn't make sense to sum these categories. You can change the summarization here to Don't summarize, so Power BI will infer more appropriate visualizations. It's also convenient to let Power BI know which data category a certain column belongs to, especially in the case of geographic data. For example, under Data category, you can select State or Province here which will allow Power BI to draw maps correctly. You can also change the way a column is sorted by clicking the dropdown menu. You can even sort this column by another column and sort Geographic Area Name by the Geographic ID for example. This will help creating an appropriate visualization when creating reports, with ordering that makes sense to the end user. Lastly, let's hide a column that has no use for the end user, for example this Geo Footnote, which seems to be always null. Right click the column name and select Hide in report view. Your data is now properly cleaned and loaded, ready for you to start creating visualizations! Let's get to the exercises.

## Lesson 02. Load and Transform Data. Instructor
1. Select Data Manufacturing.
2. Transform Data
3. Remove First Row
4. Set First Row as header
5. Change `Indusry Group` as Text
6. Change `Meaining of NICS code` in lowercase
7. Add prefix to `Industry group`. Preffix is Code:_
8. `Sales, value of shipments, or revenue ($1000)` Change to Log Natural in Scientific. Rename to  `Sales, value of shipments, or revenue ($1000)`
9. Close and Apply
10. Go to DataView
11. Select column `SUBSECTOR`. in Summarization: Don't Summarize.
12. Select `Geographic Area Name`. Change category to States or Province.
13. Sort `Geographic Area Name` click in down arrow.
14. Sort by anohter colum. `id`
15. Select `Geo Footnote` and click in down arrow. Hide column `Geo Footnote` by right clicking

### Exercise_02-01. Loading a CSV

Datasets rarely come to you exactly as you need them for data analysis. As a result, it is important to understand how to transform data using Power Query before you can start creating reports and dashboards. In this exercise, you will load a dataset, remove a row, promote a row to become the headers, and change the data type of a column.

1. Open Power BI if it isn't already open. Import `manufacturing_data.csv`
2. Remove the first row, as this includes short names for columns.
3. Promote the new first row to become headers.
4. Change the data type of the `Year`  column to become a Date.
5. **What is the value for the first row of the Year column?**
   
### Exercise_02-02. Rounding, replacement, and sorting
Power Query has a rich set of built-in functionality to solve many common problems you might run into when loading data. In this exercise, you will perform modifications to the dataset, including rounding off columns, replacing values within columns, and changing the sort operation of columns.

1. If Power Query isn't open anymore, right-click on the `manufacturing_data`  table in the _fields_  section of the _Data View_  and select "Edit Query".
2. Due to a database error the sales value accidentally multiplied its value by itself. Your task is to revert it back to its original value by taking the square root. Navigate to the `Sales, value of shipments, or revenue ($1,000)`  column and use the _Transform_  menu to take the square root of this value.
3. The United States Census Bureau informed us that a data loading error occurred in `Annual payroll ($1,000)` . It seems that the value "13356360" needs to be "1335636" instead. Replace the appropriate values. Confirm and save your data modeling changes and return to Power BI.
4. Go to the _Data_  view. You are asked to investigate "Aerospace product and parts manufacturing", which can be found in the `Meaning of NAICS code`  column. Sort the `2017 NAICS Code`  column by `Meaning of NAICS code` , and then sort it in ascending order. By doing so, data for "Aerospace product and parts manufacturing" will be shown in the top rows, which will help you answer the final question of this exercise.
5. Change the number of decimal places of the `Sales, value of shipments, or revenue ($1,000)`  column to one decimal place.
6. **What is the first value of the "Sales, value of shipments, or revenue ($1,000)" column for "Aerospace product and parts manufacturing" ?**


### Exercise_02-03. Data categorization and visibility
In the previous exercise, you've performed some data modeling steps outside of Power Query. In this exercise, you'll expand on that; there are more important attributes on columns which can enhance the user experience. You will look at two of these: data categories and visibility. Your manager asks you to give an overview of the average number of employees working in manufacturing per state, and you decide to show this on a map.

1. If you're not already in the the Data  view, go there and change the data category for the `Geographic Area Name`  to "State or Province".
2. Select the (empty) `2017 NAICS Footnote`  column and hide it from the report view.
3. Navigate to the Report  view and add a _Map_  visual to the current page. Add `Geographic Area Name`  as the _Location_  and `Number of employees`  as the _Size_. Change the aggregation of `Number of employees` to "Average".
4. **How many employees were there on average over all NAICS codes for the state of Alabama?**

### Exercise_02-04. Working with string columns

Changing the formatting of text in columns can improve the experience for end users. Something as simple as adding a common prefix or changing the casing of a string can make it easier for business users to work with a system. Your manager appreciated your work of having the number of employees displayed on a map. To further improve the user experience, you decide to add a filter for NAICS code, to easily drill down per industry.


1. Return Power Query
2. Change the casing of the `Meaning of NAICS Code` column to "Capitalize Each Word". Change the casing of the `Geographic Area Name` column to "UPPERCASE".
3. On the `2017 NAICS code` column, add a prefix of "MANU-" before each value.
4. Apply the changes and return to the _Report view_.
5. Add a slicer and use `2017 NAICS code`  as the _Field_
6. **On average, how many employees worked in the manufacturing industry code MANU-3121 in Alaska?**

## Lesson 03. Shaping Tables. Database Normalization. Instructor 

### Exercise_03-01. 

Power BI. 
   - Create relationship 
   - Create visualizations

Power Query 
   - Query Merging 
   - Query Appending
   -  Column Splitting

## Lesson 04. Merging And Appending Queries. Instructor

1. Load "Timeseries_1978.csv"
2. Select "Transform Data" ---> PowerQuery
3. Remove First Row
4. Second Row as Header
5. select New Source and then Text/CSV. This table comes from the year 1979.
6. Apply same operations First Dataset
7. To create a new table with the 1978 and 1979 tables appended, you can select Append Queries in the Combine section, and then choose between Append Queries or Append Queries as New
8. Let's rename Append1 to 1978-1979 for clarity.
9. Copy this 1978-1979 table by right clicking and selecting Duplicate.
10. I'll use the acronym EAC and remove all columns but Establishment age code and its meaning. Right click
11. contains a lot of duplicates which you can remove by right clicking and selecting Remove Duplicates. EAC table is now a reference or lookup table
12. Remove the meaning of Establishment age code in our appended table and use this column as the key to the EAC table.
13. We just want to keep the last two characters from the ID column. In the Transform menu, under the Extract option I'm going to choose Last Characters

### Exercise_04-01. Breaking a file into multiple tables

Frequently, a data scientist or business analyst will receive a single, wide file containing a variety of fields. It's often desirable to break out a single table into a more structured format in order to reduce duplication (thus saving space). In addition, if you are breaking out a reference table from a wide table, this can make it easier for certain visuals such as slicers to show the appropriate options available. In the next chapter, we will expand on this, but for now, create your own lookup table on NAICS codes.

0. 1_5_split_table
1. Open the Power BI Desktop file named 1_5_split_table.pbix  in the Exercises folder on the Desktop and go to Power Query.
2. Duplicate the `Manufacturing Data`  table and rename it to `NAICS`
3. In this new `NAICS`  table, keep only `2017 NAICS` code  and `Meaning of NAICS` code Remove the duplicate codes from `2017 NAICS code`
4. Which "Meaning of NAICS code" is shown on the 4th row of the NAICS table?. 
   - Grain and oilseed milling
   - Manufacturing
   - Food manufacturing

### Exercise_04-02. Appending files
Sometimes, you may receive data sets split into several separate files. A common example is when the data is split by year to reduce bandwidth costs or keep file sizes smaller. Being able to combine these datasets together allows you to visualize data across those different datasets and present a single, consistent table for business users. You've just received an email from a colleague, with three datasets attached. He was about to append them using Excel, but luckily, you know how to do this in a flash using Power Query, so you can repeat the process later when the three datasets get updated.

1. Within Power Query, load each of the following files as new datasets: `Timeseries_1979.csv`, `Timeseries_1980.csv`, `Timeseries_1981`.csv
2. For each of the tables you just loaded, remove the first row and use the new first row as headers.
3. Create a new table, called `Establishments by Age` , with all of the `Timeseries_19XX`  tables appended.
4. Apply the Power Query changes and return to the Report  view in Power BI. Hide all separate `Timeseries_19XX`  tables.
5. Create a _Clustered bar chart_  visual. From the `Establishments by Age`  table use the `Meaning of Establishment age code`  as _Axis_  and `Number of employees`  for the _Values_.
6. **How many employees were hired at firms which had existed for two years?**

### Exercise_04-03. Column Extraction
Often, multiple relevant features will be packed together in one column, or a single feature may have extraneous information. Power Query has a set of functionalities intended to make it easy to extract values from a column. The manufacturing dataset contains a column with ranges of percentage of total employees. You realize that it could be useful to split these ranges into their low and high limits, since the company you work for uses only the high limits of the range for their monthly reports. 

1. Go to Power Query and select the `Manufacturing Data`  table. Navigate to the last column, which should be `Range indicating percent of total employees`.
2. Duplicate the `Range indicating percent of total employees` column **twice**
3. From the first duplicated column, only keep the numbers before the first percent sign (%). You can use "%" as a delimiter. Change the resulting column's data type to "Whole Number" and rename the column to `Low Range Total Employees`.
4. From the second duplicated column, only keep the numbers before the second percent sign (%). First extract the last four characters, then extract again using "%" as a delimiter. Change the resulting column's data type to "Whole Number" and rename the column to `High Range Total Employees`.
5. Close and apply your steps and create new page with a clustered column chart visual. From `Manufacturing Data` , use the `High Range Total Employees`  column as the _Axis_  and `First-quarter payroll ($1,000)`  for the _Values_
6. **Which is the second-largest "High Range Total Employees" category in terms of payroll?**