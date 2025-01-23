-- Write your PostgreSQL query statement below
SELECT 
    St.student_id, 
    St.student_name, 
    Su.subject_name, 
    COALESCE(COUNT(Ex.student_id), 0) as attended_exams
FROM 
    Students as St 
CROSS JOIN
    Subjects as Su
LEFT JOIN 
    Examinations as Ex
ON 
    St.student_id = Ex.student_id 
    AND Su.subject_name = Ex.subject_name
GROUP BY 
    St.student_id, 
    St.student_name, 
    Su.subject_name
ORDER BY 
    St. student_id