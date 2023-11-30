SELECT good_type_name,
	SUM(amount * unit_price) as costs
from GoodTypes
	join Goods on Goods.type = GoodTypes.good_type_id
	JOIN Payments on Payments.good = Goods.good_id
where YEAR(date) = 2005
GROUP BY good_type_name