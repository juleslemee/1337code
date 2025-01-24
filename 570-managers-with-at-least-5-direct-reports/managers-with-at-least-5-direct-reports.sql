-- Write your PostgreSQL query statement below
SELECT E.name
FROM Employee AS E
JOIN Employee AS E2
ON E.id = E2.managerId
GROUP BY E.id, E.name
HAVING COUNT(E2.id) >= 5;