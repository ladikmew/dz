SELECT member_name, sum(unit_price*amount) as costs from FamilyMembers
join Payments on Payments.family_member =FamilyMembers.member_id 
where date like "2005-06%"
group by member_name 
