/*
Query the two cities in STATION with the shortest and longest CITY names, 
as well as their respective lengths (i.e.: number of characters in 
the name). If there is more than one smallest or largest city, choose the 
one that comes first when ordered alphabetically.

The STATION table is described as follows:
(./pictures/station_table.png)
*/

SELECT CITY, LENGTH(CITY) FROM STATION
    ORDER BY 2, 1
    LIMIT 1;
    
SELECT CITY, LENGTH(CITY) FROM STATION
    ORDER BY 2 DESC, 1
    LIMIT 1;