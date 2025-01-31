/* Write your T-SQL query statement below */
SELECT 
FORMAT(T.trans_date, 'yyyy-MM') as 'month',
T.country,
COUNT(T.state) as trans_count,
COUNT(CASE WHEN T.state = 'approved' THEN 1 ELSE NULL END) as approved_count,
SUM(T.amount) as trans_total_amount,
SUM(CASE WHEN T.state = 'approved' THEN T.amount ELSE 0 END) as approved_total_amount
FROM Transactions as T
GROUP BY FORMAT(T.trans_date, 'yyyy-MM'), T.country
ORDER BY FORMAT(T.trans_date, 'yyyy-MM'), T.country DESC