SELECT good_type_name
from GoodTypes
where good_type_id not in (
		SELECT DISTINCT good_type_id
		from FamilyMembers
			join Payments on Payments.family_member = FamilyMembers.member_id
			join Goods on Goods.good_id = Payments.good
			join GoodTypes on GoodTypes.good_type_id = Goods.type
		WHERE YEAR(date) = 2005
	)