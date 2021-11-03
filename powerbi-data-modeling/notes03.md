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

##

### Exercise. Cardinality

## Date dimensions and relationships in Power BI

### Exercise. Create a year dimension

### Exercise. Extend the year dimension.

### Exercise. Composite key relationships

## Granularity, measures, and hierarchies

### Exercise. Hidden hierarchies

## Hierarchies and measures in Power BI

### Exercise. Build a hierarchy

### Exercise. Change the granularity of a query

### Exercise. Measures and quick measures
