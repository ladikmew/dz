SELECT count(*) as count
from Class
	join Student_in_class on Student_in_class.class = Class.id
WHERE name = "10 B"