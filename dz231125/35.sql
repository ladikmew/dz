SELECT count(classroom) as count
from (
		SELECT DISTINCT classroom
		from Schedule
		WHERE date = "2019-09-02"
	) as t