from geopy.geocoders import Nominatim
from geopy import distance


GLASGOW_SUBWAY = 10.5

geocoder =  Nominatim(user_agent="MyApp")

def getDistance(origin, destination):
    origin_tuple = (origin.latitude, origin.longitude, origin.altitude)
    destination_tuple = (destination.latitude, destination.longitude, destination.altitude)
    return distance.distance(origin_tuple, destination_tuple).km




print("Enter a city of origin")
origin = input("Enter City: ")
print("Enter destination")
destination = input("Enter City: ")

origin_location = geocoder.geocode(origin)
destination_location = geocoder.geocode(destination)

distance = getDistance(origin_location, destination_location)

print(f"{origin} to {destination} is {distance} km")
times_around_subway = distance / GLASGOW_SUBWAY
print(f"This would be the equivalent of going around the Glasgow Subway {times_around_subway} times")
subway_time = 24 * times_around_subway
if subway_time < 60:
    print(f"This would take {subway_time} minutes to cover that distance")
else:
    hours = subway_time // 60
    minutes = subway_time % 60
    print(f"This would take {hours} hours and {minutes} minutes to cover that distance")
    


