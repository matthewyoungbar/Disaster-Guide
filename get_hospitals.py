from googleplaces import GooglePlaces, types, lang
import requests
import json
lat= input("input a latitute: ")
lng= input("input a longitude: ")
API_KEY = 'AIzaSyA13MoccnqSpa-p4ZWvfU96Za9VI8dFp2U'
google_places = GooglePlaces(API_KEY)
f = open("hospitals.json", 'w')
query_result = google_places.nearby_search(lat_lng ={'lat': lat, 'lng': lng}, radius = 5000, types =[types.TYPE_HOSPITAL])
if query_result.has_attributions:
    print (query_result.html_attributions)
f.write('hospitals = \'[')
for place in query_result.places:
    f.write('{"name": "' + place.name.replace("'", "") + '", "Latitude": ' +
            str(place.geo_location['lat']) + ', "Longitude": ' + str(place.geo_location['lng']) + '}, ')
f.write('{}]\';')
f.close()
