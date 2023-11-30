SELECT trip,
	count(passenger) as count
FROM Pass_in_trip
GROUP by trip
ORDER by count DESC