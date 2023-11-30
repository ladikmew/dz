SELECT name,
	count(student) as count
from Student_in_class
	join Class on Class.id = Student_in_class.class
GROUP by Class.id
ORDER by count DESC