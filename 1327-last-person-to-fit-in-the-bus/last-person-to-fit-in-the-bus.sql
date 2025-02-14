/* Write your T-SQL query statement below */
SELECT TOP(1) person_name
FROM(
    SELECT person_name, turn, SUM(weight) OVER (ORDER BY turn) AS cumulative_weight
    FROM Queue
) AS subQ
WHERE subQ.cumulative_weight <= 1000
ORDER BY subQ.turn DESC