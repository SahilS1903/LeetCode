# Write your MySQL query statement below
select date_format(t.trans_date,'%Y-%m') as month,
t.country,
count(id) as trans_count,
sum(if(t.state='approved',1,0)) as approved_count,
sum(t.amount) as trans_total_amount,
sum(if(t.state='approved',t.amount,0)) as approved_total_amount
from transactions t
group by month,t.country