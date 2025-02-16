/* Write your T-SQL query statement below */
SELECT E.employee_id
FROM Employees as E
WHERE E.manager_id IS NOT NULL
AND NOT EXISTS (
    SELECT 1
    FROM Employees as Managers
    WHERE E.manager_id = Managers.employee_id
) AND E.salary < 30000
ORDER BY E.employee_id