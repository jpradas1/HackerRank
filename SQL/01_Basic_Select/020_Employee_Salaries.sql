/*
Write a query that prints a list of employee names (i.e.: the name 
attribute) for employees in Employee having a salary greater than `$2000` 
per month who have been employees for less than 10 months. Sort your result
by ascending employee_id.

The Employee table containing employee data for a company is described as 
follows:
(./pictures/employee_table.png)
*/

SELECT name FROM Employee
    WHERE months < 10
    AND salary > 2000
    ORDER BY employee_id;