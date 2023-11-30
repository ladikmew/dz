SELECT FLOOR(
		COUNT(id) * 100 /(
			SELECT COUNT(student)
			from Student_in_class
		)
	) as percent
from Student
where YEAR(birthday) = "2000"