SELECT DISTINCT name
from Class
	JOIN Schedule on Schedule.class = Class.id
	JOIN Teacher on Teacher.id = Schedule.teacher
WHERE last_name = "Krauze"