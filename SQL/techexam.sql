SELECT department.dept_id, COUNT(employee.dept_id), SUM(employee.salary) AS sum_of_salary
FROM department
INNER JOIN employee on department.dept_id = employee.dept_id
GROUP BY department.dept_id
ORDER BY dept_id ASC;