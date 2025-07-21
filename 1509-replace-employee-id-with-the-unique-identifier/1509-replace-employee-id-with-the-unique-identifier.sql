# Write your MySQL query statement below
select em.unique_id,e.name 
from employeeUni  em
right join employees  e
on em.id=e.id