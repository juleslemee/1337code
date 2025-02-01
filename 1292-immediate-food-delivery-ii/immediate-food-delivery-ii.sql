/* Write your T-SQL query statement below */


-- I want to count how many order_date = customer_pref_delivery_date (immediate orders) 
-- / order_date (all orders, immediate+scheduled)
-- all of these have to be the first order of a customer, i.e. the earliest order_date
WITH first_immediate AS (
    SELECT d.customer_id, MIN(d.order_date) as mins
    FROM Delivery as d
    WHERE d.order_date = (
        SELECT MIN(d2.order_date) 
        FROM Delivery d2
        WHERE d2.customer_id = d.customer_id
    )
    AND d.order_date = d.customer_pref_delivery_date
    GROUP BY d.customer_id
), 
all_first AS (
    SELECT d3.customer_id, MIN(order_date) as mins3
    FROM Delivery as d3
    GROUP BY d3.customer_id
)

SELECT 
ROUND(COUNT(fi.customer_id)*100.0/ COUNT(af.customer_id), 2) as immediate_percentage
FROM
first_immediate as fi
FULL OUTER JOIN 
all_first as af
ON
fi.customer_id = af.customer_id