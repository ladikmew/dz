SELECT distinct name
from Passenger
	JOIN Pass_in_trip on Pass_in_trip.passenger = passenger.id
	join Trip on Trip.id = Pass_in_trip.trip
where town_to = "Moscow"
	and plane = "TU-134"