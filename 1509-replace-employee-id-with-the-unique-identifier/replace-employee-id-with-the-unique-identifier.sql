/* Write your T-SQL query statement below */
SELECT EUNI.unique_id, E.name
FROM Employees as E
LEFT JOIN EmployeeUNI as EUNI ON E.id = EUNI.id