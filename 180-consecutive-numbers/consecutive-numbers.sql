/* Write your T-SQL query statement below */

SELECT DISTINCT L.num as ConsecutiveNums
FROM Logs AS L
LEFT JOIN Logs AS L2 ON (L.id+1) = L2.id
LEFT JOIN Logs AS L3 ON (L.id+2) = L3.id
WHERE L.num = L2.num AND L2.num = L3.num
