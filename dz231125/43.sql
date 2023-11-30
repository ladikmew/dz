SELECT last_name
from Teacher
	JOIN Schedule on Schedule.teacher = Teacher.id
	JOIN Subject on Subject.id = Schedule.subject
where name = "Physical Culture"
ORDER BY last_name