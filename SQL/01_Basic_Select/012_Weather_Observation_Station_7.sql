/*
Query the list of CITY names ending with vowels (a, e, i, o, u) from 
STATION. Your result cannot contain duplicates.

The STATION table is described as follows:
(./pictures/station_table.png)
*/

SELECT DISTINCT(CITY) FROM STATION
    WHERE CITY LIKE '%a' OR 
    CITY LIKE '%e' OR 
    CITY LIKE '%i' OR 
    CITY LIKE '%o' OR 
    CITY LIKE '%u';