SELECT 'Employees' AS Employees,   
  [Doctor], [Professor], [Singer], [Actor]  
FROM  
(
  SELECT Occupation, Name   
  FROM OCCUPATIONS
) AS SourceTable  
PIVOT  
(  
  MIN(Name)  
  FOR Occupation IN ([Doctor], [Professor], [Singer], [Actor])  
) AS PivotTable;