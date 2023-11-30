SELECT count(student) * 100 /(
		SELECT count(student)
		from Student_in_class
	) as percent
from Student_in_class
	JOIN Class on Class.id = Student_in_class.class
WHERE name = "10 A"