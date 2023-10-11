/*
Write a query identifying the type of each record in the TRIANGLES table 
using its three side lengths. Output one of the following statements for 
each record in the table:

1. Equilateral: It's a triangle with  sides of equal length.
2. Isosceles: It's a triangle with  sides of equal length.
3. Scalene: It's a triangle with  sides of differing lengths.
4. Not A Triangle: The given values of A, B, and C don't form a triangle.

IF STATEMENT IN SQL

SELECT IF(500<1000, "YES", "NO");
>>> YES

The TRIANGLES table is described as follows:
(./pictures/triangles_table.png)
*/

SELECT IF(A+B<=C OR A+C<=B OR B+C<=A,"Not A Triangle",
    IF(A=B AND B=C,"Equilateral",
    IF(A=B OR B=C OR C=A,"Isosceles","Scalene")))
    FROM TRIANGLES;