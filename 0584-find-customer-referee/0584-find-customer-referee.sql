# Write your MySQL query statement below
Select name
from Customer 
where ifnull(Customer.referee_id,0) != 2