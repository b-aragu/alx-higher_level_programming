DBMS (Database management system)
__Atomicity__ - If a transaction fail, the result will be like it never happened
__Consistency__ - You can define rules for your data and expect that the data abides by the rules or else transaction fails. 
__Isolation__ - You can ran two operations at the same time and expect that the result is as though they were ran one after another.
__Durability__ - Unplug your server, boot it back up and it doesn't loose any data.
**(ACID)**, **CRUD**
- Create some data
- Read some data
- Update some data
- Destroy some data.

#### Types of DBMS
__1. Hierachical__ - parent child relationship.
__2. Network DBMS__ - Supports many to many relationships
__3. Relational DBMS__ - defines relations in form of tables. mysql, oracle
__4. Object oriented relational DBMS__ - support storage of new data types.
#### Querying  multiple tables.
- The __`JOIN`__ clause can be used to combine rows from two or more tables in a query result. Does this by finding a related column between the tables and sort the results approapriately in the output.
- A `SELECT` statement that includes a `JOIN`
```mysql
SELECT table1.column1, table2.column2
FROM table1
JOIN table2 ON table1.related_column=table2.related_column;
```
- __`Inner Join`__ - Means that is selects all the records that have matching values in both tables and prints them to the result set, excluding any unmatching records.
- __`Outer join`__ - returns all the record from one table. Clauses are written either as `LEFT JOIN` or `RIGHT JOIN`
- __`LEFT JOIN`__ - returns all the records of the left table and  only te matching records from the right table
```mysql
SELECT table1.column1, table2.column2
FROM table1
LEFT JOIN table2 ON table1.related_column=table2.related_column;
```
- __`RIGHT JOIN`__ - returns all the records of the right table including only matching records in the right table.
```mysql
SELECT table1.column1, table2.column2
FROM table1
RIGHT JOIN table2 ON table1.related_column=table2.related_column;
```
- For right or left join, if there are no matching records, a null value or a blank value is returned.

### Data definition Language
- Used to build and modify the structure of your tables and objects in the database.
```mysql
CREATE TABLE <table name> ( <attribute name 1> <data type 1>, ... <attribute name n> <data type n>);
```
- Alter table statement maybe used to specify primary and foreign keys constraints, as well as to make other modifications to the table structure.
```mysql
ALTER TABLE <table name> 
ADD CONSTRAINT <constraint name> PRIMARY KEY (<attribute list>);
```
- Foreign key constraints are a bit more complicated since we have to specify both the FK attribute in child attribute , and the PK attribute that they link up to the parent.
```mysql
ALTER TABLE <table name> 
ADD CONSTRAINT <constraint name> FOREIGN KEY (<attribute list>) 
REFERENCES <parent table name> (<attribute list>);
```
- If you totally mess things up and you want to start over, you can always get rid of any object you have created with a drop statement.
```mysql
DROP TABLE <table name>;
ALTER TABLE <table name>
DROP CONSTRAINT <constraint name>;
```
### Data manipulation Language
- Statements that are used to work with the data in tables.
- Insert is used to add new rows to the table.
```mysql
INSERT INTO <table name>
VALUES (<value 1>, ... <value n>);
```
- Update is used to change values already in the table.
```mysql
UPDATE <table name> 
SET <attribute> = <expression> 
WHERE <condition>;
```
- Delete statement just that does that for row in a table.
```mysql
DELETE FROM <table name>
WHERE <condition>;
```
- If WHERE clause is omitted, every row in the table is deleted.
- COMMIT and ROLLBACK statements are used to manage transactions.
