select good_name,
	unit_price
from goods
	join Payments on Goods.good_id = Payments.good
	join GoodTypes on GoodTypes.good_type_id = Goods.type
where unit_price =(
		SELECT max(unit_price)
		from payments
			join Goods on Goods.good_id = Payments.good
			join GoodTypes on GoodTypes.good_type_id = Goods.type
		where good_type_name = "delicacies"
	)