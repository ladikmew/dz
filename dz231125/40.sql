SELECT name as subjects
from Subject
	join Schedule on Schedule.subject = Subject.id
	join Teacher on Schedule.teacher = Teacher.id
where last_name = "Romashkin"
	and first_name LIKE "P%"
	and middle_name like "P%"