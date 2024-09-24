# Write your MySQL query statement below
select Prices.product_id , ifnull(Round(Sum(units*price)/sum(units),2),0) as average_price
from Prices Left Join UnitsSold 
on UnitsSold.product_id = Prices.product_id and 
UnitsSold.purchase_date Between Prices.start_date and Prices.end_date
group by Prices.product_id 
