/* Write your T-SQL query statement below */
SELECT 
CONVERT(VARCHAR(7), T.trans_date, 120) AS 'month',
T.country,
COUNT(T.state) as trans_count,
COUNT(CASE WHEN T.state = 'approved' THEN 1 ELSE NULL END) as approved_count,
SUM(T.amount) as trans_total_amount,
SUM(CASE WHEN T.state = 'approved' THEN T.amount ELSE 0 END) as approved_total_amount
FROM Transactions as T
GROUP BY CONVERT(VARCHAR(7), T.trans_date, 120), T.country
ORDER BY CONVERT(VARCHAR(7), T.trans_date, 120), T.country DESC