/* Write your T-SQL query statement below */
SELECT employee_id, department_id
FROM (
    SELECT employee_id, department_id, primary_flag,
           COUNT(*) OVER (PARTITION BY employee_id) AS dept_count
    FROM Employee
) subquery
WHERE primary_flag = 'Y' OR dept_count = 1