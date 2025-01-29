-- Write your PostgreSQL query statement below
WITH UserCount AS (
    SELECT COUNT(user_id) AS total_users FROM Users
)
SELECT 
    contest_id, 
    ROUND((COUNT(user_id) * 100.0 / (SELECT total_users FROM UserCount))::NUMERIC, 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;
