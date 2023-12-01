SELECT status,
	member_name,
	sum(unit_price * amount) as costs
from FamilyMembers
	join Payments on Payments.family_member = FamilyMembers.member_id
	join Goods on Goods.good_id = Payments.good
	join GoodTypes on GoodTypes.good_type_id = Goods.type
WHERE good_type_name = "entertainment"
GROUP BY status,
	member_name