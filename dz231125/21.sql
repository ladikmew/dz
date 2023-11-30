SELECT distinct status
from FamilyMembers
	left join Payments on Payments.family_member = FamilyMembers.member_id
	left join Goods on Goods.good_id = Payments.good
where good_name = "potato"