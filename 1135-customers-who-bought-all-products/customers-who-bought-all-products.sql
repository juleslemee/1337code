/* Write your T-SQL query statement below */
-- if the group by count is greater than the length of the product table
-- nevermind. they could have just bought the same thing many times.
-- maybe I can remove duplicates or do some kind of inner join
SELECT 
customer_id
FROM(
    SELECT
    customer_id, COUNT(DISTINCT product_key) as pCount
    FROM
    Customer
    GROUP BY
    customer_id
) as productCount
WHERE pCount >= (SELECT COUNT(*) FROM Product)