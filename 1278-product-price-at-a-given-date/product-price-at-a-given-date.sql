/* Write your T-SQL query statement below */
WITH RankedPrices AS (
    SELECT
    product_id,
    new_price AS price,
    ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS rn
    FROM Products
    WHERE change_date <= '2019-08-16'
)
SELECT product_id, price
FROM RankedPrices
WHERE rn = 1

UNION ALL

SELECT DISTINCT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM RankedPrices)