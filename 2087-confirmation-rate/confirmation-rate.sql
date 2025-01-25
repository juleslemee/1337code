/* Write your T-SQL query statement below */

SELECT 
S.user_id, ROUND(CAST(ISNULL(C.confirms, 0) AS FLOAT) / ISNULL(T.totals, 1), 2) AS confirmation_rate
FROM 
Signups as S
LEFT JOIN
    (SELECT user_id, COUNT(action) as confirms 
    FROM Confirmations 
    WHERE action = 'confirmed' 
GROUP BY user_id) AS C
ON
S.user_id = C.user_id
LEFT JOIN
    (SELECT user_id, COUNT(action) as totals
    FROM Confirmations 
    GROUP BY user_id) AS T
ON
C.user_id = T.user_id