SELECT count(*) as count
from Teacher
	JOIN Schedule on Schedule.teacher = Teacher.id
WHERE date = "2019-08-30"
	and last_name = "Krauze"