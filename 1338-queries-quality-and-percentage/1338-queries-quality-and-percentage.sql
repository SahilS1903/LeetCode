# Write your MySQL query statement below
select query_name ,
round((sum(rating/position))/count(q.Query_name),2) as quality ,
round(sum(if(rating<3,1,0))/count(q.Query_name)*100,2) as poor_query_percentage
from queries q
group by q.query_name