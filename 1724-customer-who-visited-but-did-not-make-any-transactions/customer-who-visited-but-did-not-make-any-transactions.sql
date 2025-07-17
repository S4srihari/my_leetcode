# Write your MySQL query statement below
SELECT customer_id, count(customer_id) as count_no_trans FROM
Visits v left Join Transactions t on v.visit_id = t.visit_id 
Where  t.transaction_id is null
group by customer_id;