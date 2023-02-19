from FlightRadar24.api import FlightRadar24API
import time
from geopy.geocoders import Nominatim
geocoder = Nominatim(user_agent = 'your_app_name')
import requests
import json

def findFlight(flight_number):
    api = FlightRadar24API()
    flights = api.get_flights()
    for flight in flights:
        if (flight.number == flight_number):
            return api.get_flight_details(flight.id)
    return None


print("Gimme a plane yo!")
flight_number = input("Plane Number: ")
flight_details = findFlight(flight_number)
#print(flight_details["trail"][0])
#try:
coordinates = (flight_details["trail"][0]["lat"], flight_details["trail"][0]["lng"])
location = geocoder.reverse(coordinates)
print(f"Origin: {flight_details['airport']['origin']['name']}")
print(f"Destination: {flight_details['airport']['destination']['name']}")
print(f"The plane is at coordinates {coordinates}")

url = f"https://api.what3words.com/v3/convert-to-3wa?coordinates={coordinates[0]},{coordinates[1]}&key=AAY46H1S"
response = requests.get(url)
data = response.json()
if not location:
    
    print(f"Nearest location is {data['nearestPlace']}")
else:
    print(location)
print(f"What3Words = {data['words']}")
    
    
    
#except:
    #print("We couldn't find the plane")