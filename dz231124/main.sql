--15
SELECT time_in from trip
join Pass_in_trip on trip.id=Pass_in_trip.trip 
join passenger on passenger.id=Pass_in_trip.passenger 
where name="Steve Martin" and town_to='London'
--14
SELECT DISTINCT town_to
from trip
	join Pass_in_trip on trip.id = Pass_in_trip.trip
	join passenger on passenger.id = Pass_in_trip.passenger
where name = "Bruce Willis"
