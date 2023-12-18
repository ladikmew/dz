--16
SELECT t2.name,
	t1.count
from (
		SELECT passenger,
			COUNT(*) as count
		from Pass_in_trip
		GROUP BY passenger
	) AS t1
	LEFT JOIN passenger as t2 ON t2.id = t1.passenger
ORDER by t1.count DESC,
	t2.name

--17
SELECT member_name,
	status,
	SUM(amount * unit_price) as costs
from FamilyMembers
	left join Payments on FamilyMembers.member_id = Payments.family_member
where YEAR(date) = 2005
GROUP BY member_name,
	status
HAVING costs > 0

--18
SELECT member_name
from FamilyMembers
where birthday =(
		SELECT min(birthday)
		from FamilyMembers
	)

--19
SELECT distinct status
from FamilyMembers
	left join Payments on Payments.family_member = FamilyMembers.member_id
	left join Goods on Goods.good_id = Payments.good
where good_name = "potato"

--20
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

--21
SELECT good_name
from Goods
	join Payments on Payments.good = goods.good_id
group by good_id
having count(good) > 1

--22
SELECT member_name
from FamilyMembers
where status = "mother" -- GROUP by member_name

--23
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

--24
SELECT member_name,
	sum(unit_price * amount) as costs
from FamilyMembers
	join Payments on Payments.family_member = FamilyMembers.member_id
where date like "2005-06%"
group by member_name

--25
SELECT good_name
from Goods
where good_id not in (
		SELECT good
		from Payments
		where YEAR(date) = 2005
	)
--26
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

--27
SELECT good_type_name,
	SUM(amount * unit_price) as costs
from GoodTypes
	join Goods on Goods.type = GoodTypes.good_type_id
	JOIN Payments on Payments.good = Goods.good_id
where YEAR(date) = 2005
GROUP BY good_type_name
--28
SELECT count(*) as count
from Trip
WHERE town_to = "Rostov"
	and town_from = "Moscow"

--29
SELECT distinct name
from Passenger
	JOIN Pass_in_trip on Pass_in_trip.passenger = passenger.id
	join Trip on Trip.id = Pass_in_trip.trip
where town_to = "Moscow"
	and plane = "TU-134"

--30
SELECT trip,
	count(passenger) as count
FROM Pass_in_trip
GROUP by trip
ORDER by count DESC

--31
SELECT *
from FamilyMembers
where member_name LIKE "%Quincey"

--32
SELECT FLOOR(AVG(YEAR(CURDATE()) - year(birthday))) as age
from FamilyMembers

--33
SELECT AVG(unit_price) as cost
from Payments
WHERE good in(
		SELECT good_id
		from Goods
		WHERE good_name = "red caviar"
			or good_name = "black caviar"
	)

--34
SELECT count(*) as count
from Class
where name LIKE "10%"

--35
SELECT count(classroom) as count
from (
		SELECT DISTINCT classroom
		from Schedule
		WHERE date = "2019-09-02"
	) as t

--36
SELECT *
from Student
where address LIKE "ul. Pushkina%"

--37
SELECT min(TIMESTAMPDIFF(YEAR, birthday, CURDATE())) as year
from Student

--38
SELECT count(*) as count
from Student
WHERE first_name = "Anna"

--39
SELECT count(*) as count
from Class
	join Student_in_class on Student_in_class.class = Class.id
WHERE name = "10 B"

--40
SELECT name as subjects
from Subject
	join Schedule on Schedule.subject = Subject.id
	join Teacher on Schedule.teacher = Teacher.id
where last_name = "Romashkin"
	and first_name LIKE "P%"
	and middle_name like "P%"

--41
SELECT start_pair
from Timepair
WHERE id = "4"

--42
SELECT TIMEDIFF(
		(
			SELECT end_pair
			from Timepair
			where id = "4"
		),
		start_pair
	) as time
from Timepair
WHERE id = "2"

--43
SELECT last_name
from Teacher
	JOIN Schedule on Schedule.teacher = Teacher.id
	JOIN Subject on Subject.id = Schedule.subject
where name = "Physical Culture"
ORDER BY last_name

--44
SELECT (2023 - YEAR(min(birthday))) as max_year
from Student
where id in (
		SELECT DISTINCT student
		from Student_in_class
		where class in (
				SELECT id
				from Class
				where name like "10%"
			)
	)

--45
SELECT classroom
from (
		SELECT *,
			MAX(cnt) Over() as max_cnt
		FROM (
				SELECT classroom,
					count(*) as cnt
				from Schedule
				group by classroom
			) as t
	) as t1
where t1.cnt = t1.max_cnt

--46
SELECT DISTINCT name
from Class
	JOIN Schedule on Schedule.class = Class.id
	JOIN Teacher on Teacher.id = Schedule.teacher
WHERE last_name = "Krauze"

--47
SELECT count(*) as count
from Teacher
	JOIN Schedule on Schedule.teacher = Teacher.id
WHERE date = "2019-08-30"
	and last_name = "Krauze"

--48
SELECT name,
	count(student) as count
from Student_in_class
	join Class on Class.id = Student_in_class.class
GROUP by Class.id
ORDER by count DESC

--49
SELECT count(student) * 100 /(
		SELECT count(student)
		from Student_in_class
	) as percent
from Student_in_class
	JOIN Class on Class.id = Student_in_class.class
WHERE name = "10 A"

--50
SELECT FLOOR(
		COUNT(id) * 100 /(
			SELECT COUNT(student)
			from Student_in_class
		)
	) as percent
from Student
where YEAR(birthday) = "2000"