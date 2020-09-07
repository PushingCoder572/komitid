from geopy import Nominatim

locator = Nominatim(user_agent='myGeocoder')
location = locator.geocode("Kristinelundsvägen 27")
print(f'Latitude = {location.latitude}, Longitude = {location.longitude}')

#http://api.sl.se/api2/TravelplannerV3_1/trip.json?key=6828b3e5b4b04737b4311891e825e913&originCoordLat=59437629&originCoordLong=18115224&destId=9668&Date=2020-09-04&Time=09:00&searchForArrival=10


#     api.sl.se/api2/nearbystopsv2.json?key=71559263e234458bbc45887f651c6e2&originCoordLat=594380336&originCoordLong=181112802