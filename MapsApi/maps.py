import requests
import creds
"""
Retrieves the latitude and longitude coordinates for a given location.
Args:location (str): The location to geocode.
Returns:tuple: The latitude and longitude coordinates.
    """
def get_latitude_longitude(location):
    response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={location}, Stockholm, Sweden&key={creds.api_key}')
    
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            result = data['results'][0]
            lat = result['geometry']['location']['lat']
            lng = result['geometry']['location']['lng']
            return lat, lng

    return None, None
#Adding multiple locations
locations = ['Gustavslund', 'Östra Ormsta', 'Kårsta torg', 'Vallentuna station', 'Markims Husby', 'Uthamra', 'Kårsta station']

#Creating an empty list to store the locations
coordinates = []

for location in locations:

# Retrieve latitude and longitude for the location
    latitude, longitude = get_latitude_longitude(location)
    
    if latitude and longitude:
        coordinates.append((location,latitude,longitude))
#print the coordinates

for location, latitude, longitude in coordinates:
    print(f'Location: {location}')
    print(f'Latitude: {latitude}')
    print(f'Longitude: {longitude}')
    print("------")

"""
Location: Gustavslund
Latitude: 59.32932349999999
Longitude: 18.0685808
------
Location: Östra Ormsta
Latitude: 59.32932349999999
Longitude: 18.0685808
------
Location: Kårsta torg
Latitude: 59.32932349999999
Longitude: 18.0685808
------
Location: Vallentuna station
Latitude: 59.5338921
Longitude: 18.0798404
------
Location: Markims Husby
Latitude: 59.40969579999999
Longitude: 17.9284919
------
Location: Uthamra
Latitude: 59.509968
Longitude: 18.054532
------
Location: Kårsta station
Latitude: 59.32932349999999
Longitude: 18.0685808
"""