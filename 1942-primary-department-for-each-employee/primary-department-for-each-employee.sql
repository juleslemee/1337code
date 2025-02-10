/* Write your T-SQL query statement below */
WITH EmployeeDepartmentCount AS (
    SELECT employee_id, COUNT(*) AS dept_count
    FROM Employee
    GROUP BY employee_id
)
SELECT e.employee_id, e.department_id
FROM Employee e
JOIN EmployeeDepartmentCount edc 
    ON e.employee_id = edc.employee_id
WHERE e.primary_flag = 'Y' OR edc.dept_count = 1;