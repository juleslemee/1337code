/* Write your T-SQL query statement below */


-- I want to count how many order_date = customer_pref_delivery_date (immediate orders) 
-- / order_date (all orders, immediate+scheduled)
-- all of these have to be the first order of a customer, i.e. the earliest order_date
WITH all_first AS (
    SELECT customer_id, MIN(order_date) as min_order_date
    FROM Delivery
    GROUP BY customer_id
),
first_immediate AS (
    SELECT af.customer_id, af.min_order_date
    FROM all_first AS af
    JOIN Delivery d ON d.customer_id = af.customer_id AND d.order_date = af.min_order_date
    WHERE d.order_date = d.customer_pref_delivery_date
)

SELECT 
ROUND(COUNT(fi.customer_id)*100.0/ COUNT(af.customer_id), 2) as immediate_percentage
FROM
first_immediate as fi
FULL OUTER JOIN 
all_first as af
ON
fi.customer_id = af.customer_id