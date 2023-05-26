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


location = 'sollentuna'

# Retrieve latitude and longitude for the location
latitude, longitude = get_latitude_longitude(location)

print(f'Location: {location}')
print(f'Latitude: {latitude}')
print(f'Longitude: {longitude}')
