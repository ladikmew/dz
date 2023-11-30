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