/* Write your T-SQL query statement below */
SELECT COALESCE(
    (SELECT max(num) 
    FROM (
        SELECT
        num
        FROM
        MyNumbers
        GROUP BY
        num
        HAVING
        COUNT(num) < 2
    ) as UniqueNums), 
    null) as num