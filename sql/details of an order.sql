use new_schema;
select o.ord_no,o.ord_date,o.purch_amt,c.cust_name as customer_name,c.grade,s.name,s.commission
from orders o
inner join customer c on o.customer_id=o.customer_id
inner join salesman s on s.salesman_id=c.salesman_id;
