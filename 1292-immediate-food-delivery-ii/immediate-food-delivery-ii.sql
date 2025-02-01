/* Write your T-SQL query statement below */
SELECT 
    ROUND(SUM(CASE WHEN d.order_date = d.customer_pref_delivery_date THEN 1 ELSE 0 END) 
        * 100.0 / COUNT(DISTINCT d.customer_id), 2) AS immediate_percentage
FROM Delivery d
JOIN (
    SELECT customer_id, MIN(order_date) AS min_order_date
    FROM Delivery
    GROUP BY customer_id
) first_orders 
ON d.customer_id = first_orders.customer_id 
AND d.order_date = first_orders.min_order_date;