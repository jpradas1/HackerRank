/*
Query a list of CITY names from STATION for cities that have an even 
ID number. Print the results in any order, but exclude duplicates from 
the answer.

The STATION table is described as follows:
(./pictures/station_table.png)
*/

SELECT DISTINCT(CITY) FROM STATION WHERE MOD(ID, 2) = 0;