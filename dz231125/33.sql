SELECT AVG(unit_price) as cost
from Payments
WHERE good in(
		SELECT good_id
		from Goods
		WHERE good_name = "red caviar"
			or good_name = "black caviar"
	)