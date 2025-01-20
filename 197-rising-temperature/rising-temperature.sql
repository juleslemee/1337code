-- Write your PostgreSQL query statement below
SELECT W1.id
FROM Weather as W1
JOIN Weather as W2 
ON W1.recordDate = W2.recordDate + INTERVAL '1 day'
WHERE W1.temperature > W2.temperature