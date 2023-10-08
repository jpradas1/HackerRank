/*
Query all attributes of every Japanese city in the CITY table. 
The COUNTRYCODE for Japan is JPN.

The CITY table is described as follows:
(./pictures/city_table.png)
*/

SELECT * FROM CITY
    WHERE COUNTRYCODE = 'JPN';