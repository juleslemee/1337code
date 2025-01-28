/* Write your T-SQL query statement below */
SELECT P.project_id, AVG(AY.sumE) as average_years
FROM
Project as P
LEFT JOIN
(
    SELECT project_id, ROUND(SUM(E.experience_years) * 1.0 / COUNT(E.experience_years), 2) as sumE
    FROM
    Project as P
    LEFT JOIN
    Employee as E
    ON
    P.employee_id = E.employee_id
    GROUP BY project_id
) as AY
ON P.project_id = AY.project_id
GROUP BY P.project_id
ORDER BY P.project_id