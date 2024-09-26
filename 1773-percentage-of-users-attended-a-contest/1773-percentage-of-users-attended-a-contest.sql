# Write your MySQL query statement below
Select contest_id , round(count(Distinct r.user_id)*100/count(Distinct u.user_id),2) as percentage
from Register r, Users u
group by contest_id
order by percentage Desc, contest_id Asc
