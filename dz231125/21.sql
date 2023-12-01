SELECT good_name
from Goods
	join Payments on Payments.good = goods.good_id
group by good_id
having count(good) > 1