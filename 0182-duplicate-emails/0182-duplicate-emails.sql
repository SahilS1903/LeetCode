# Write your MySQL query statement below
select email from Person Group by email Having count(email)>1