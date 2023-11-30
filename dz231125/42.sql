SELECT TIMEDIFF(
		(
			SELECT end_pair
			from Timepair
			where id = "4"
		),
		start_pair
	) as time
from Timepair
WHERE id = "2"