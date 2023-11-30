SELECT good_name
from Goods
where good_id not in (
		SELECT good
		from Payments
		where YEAR(date) = 2005
	)