/* Write your T-SQL query statement below */
SELECT P.project_id, ROUND(SUM(E.experience_years) * 1.0 / COUNT(E.experience_years), 2) as average_years
FROM
Project as P
INNER JOIN
Employee as E
ON
P.employee_id = E.employee_id
GROUP BY project_id
ORDER BY P.project_id