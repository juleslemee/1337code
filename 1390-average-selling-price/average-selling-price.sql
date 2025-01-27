/* Write your T-SQL query statement below */
SELECT
    P.product_id, COALESCE(ROUND(SUM(P.price * U.units) * 1.0 / SUM(U.units), 2), 0) AS average_price
FROM
    Prices as P
        LEFT JOIN
            UnitsSold as U
        ON
            P.product_id = U.product_id
            AND U.purchase_date BETWEEN P.start_date AND P.end_date
GROUP BY
    P.product_id
