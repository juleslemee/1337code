/* Write your T-SQL query statement below */

SELECT
E.employee_id, E.name, R.reports_count, CASE 
        WHEN R.avg_age - FLOOR(R.avg_age) >= 0.5 THEN FLOOR(R.avg_age) + 1
        ELSE FLOOR(R.avg_age)
    END AS average_age
FROM
Employees as E
INNER JOIN
(
    SELECT reports_to, COUNT(employee_id) as reports_count, AVG(CAST(age AS DECIMAL(10,2))) as avg_age
    FROM Employees 
    GROUP BY reports_to
) as R
ON
E.employee_id = R.reports_to

/*
SELECT 
    D.employee_id,
    D.name,
    D.reports_count,
    CASE 
        WHEN D.avg_age - FLOOR(D.avg_age) >= 0.5 THEN FLOOR(D.avg_age) + 1
        ELSE FLOOR(D.avg_age)
    END AS average_age
FROM (
    SELECT 
        m.employee_id,
        m.name,
        COUNT(*) AS reports_count,
        AVG(CAST(r.age AS DECIMAL(10,2))) AS avg_age
    FROM Employees AS m
    JOIN Employees AS r 
      ON r.reports_to = m.employee_id
    GROUP BY m.employee_id, m.name
) AS D
ORDER BY D.employee_id;
*/