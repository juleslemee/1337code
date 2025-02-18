SELECT 
Seat.id,
CASE 
    WHEN Seat.id % 2 != 0 THEN
    CASE
        WHEN Seat2.student IS NOT NULL 
        THEN Seat2.student 
        ELSE Seat.student 
        END
    WHEN Seat.id % 2 = 0 THEN Seat3.student
    ELSE Seat.student
    END as student
FROM Seat
LEFT JOIN (
    SELECT *
    FROM Seat
) as Seat2
ON Seat.id + 1 = Seat2.id
LEFT JOIN (
    SELECT *
    FROM Seat
) as Seat3
ON Seat.id = Seat3.id + 1