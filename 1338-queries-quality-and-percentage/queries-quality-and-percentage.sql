/* Write your T-SQL query statement below */
-- avg(rating divided by position) = 'quality'
-- count(rating less than 3)/count all = 'poor_query_percentage'

SELECT
query_name,
ROUND(AVG(rating * 1.0 / position), 2) as 'quality',
ROUND(COUNT(CASE WHEN rating < 3 THEN rating END) * 100.0 /COUNT(rating) , 2) as 'poor_query_percentage'
FROM Queries
GROUP BY
query_name