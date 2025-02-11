/* Write your T-SQL query statement below */
SELECT x, y, z, CASE WHEN (z < x+y) AND (x < y+z) AND (y < x+z) THEN 'Yes' ELSE 'No' END AS Triangle
FROM Triangle