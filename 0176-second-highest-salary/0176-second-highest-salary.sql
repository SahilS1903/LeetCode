# Write your MySQL query statement below
-- select max(salary) as SecondHighestSalary 
-- from employee
-- where salary<(
--     select max(salary) from employee
-- )



SELECT (
  SELECT distinct salary
  FROM Employee
  ORDER BY salary DESC
  LIMIT 1 OFFSET 1
) AS SecondHighestSalary;

