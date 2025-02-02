/* Write your T-SQL query statement below */
WITH fd AS (
    SELECT player_id, MIN(event_date) as first_day
    FROM Activity
    GROUP BY player_id
), lb AS (
    SELECT fd.player_id as player_id
    FROM Activity as A
    LEFT JOIN fd
    ON A.player_id = fd.player_id
    WHERE A.event_date = DATEADD(day, 1, fd.first_day)
)

SELECT ROUND(COUNT(lb.player_id) * 1.0 / COUNT(fd.player_id), 2) as fraction
FROM fd
LEFT JOIN lb
ON fd.player_id = lb.player_id

