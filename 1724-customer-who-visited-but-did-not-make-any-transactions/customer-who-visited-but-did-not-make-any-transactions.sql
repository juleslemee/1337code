-- Write your PostgreSQL query statement below
-- customer_id, COUNT(V.visit_id)-COUNT(T.visit_id)
SELECT V.customer_id, COUNT(*) as count_no_trans
FROM Visits as V
LEFT JOIN 
Transactions as T
ON V.visit_id = T.visit_id
WHERE T.transaction_id IS NULL
GROUP BY V.customer_id;

-- im not returning customers who bought AND window-shopped. 
-- i need to find a way to get the number of visits where they didn't
-- shop (in the first case 4-2 = 2)
/*
FROM Visits
GROUP BY customer_id
EXCEPT
SELECT V.customer_id, COUNT(T.visit_id)
*/