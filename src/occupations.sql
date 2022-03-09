/*
Occupations

Pivot the Occupation column in OCCUPATIONS so that each Name
is sorted alphabetically and displayed underneath its
corresponding Occupation. The output column headers should
be Doctor, Professor, Singer, and Actor, respectively.

Note: Print NULL when there are no more names corresponding
to an occupation.

Occupation will only contain one of the following values:
Doctor, Professor, Singer or Actor.
*/
SELECT    
  [Doctor], [Professor], [Singer], [Actor]  
FROM  
(
  SELECT 
    ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) row_num, 
    Name, 
    Occupation
    FROM OCCUPATIONS
    GROUP BY Occupation, Name
) AS SourceTable 
PIVOT  
(  
  MAX(Name)  
  FOR Occupation IN ([Doctor], [Professor], [Singer], [Actor])  
) AS PivotTable;