import json
import requests

from config import OPEN_WEATHER_API_KEY


def get_city_coords(city, api_key):
    # Define the API endpoint URL
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': city,
        'limit': 5,
        'appid': api_key,
    }

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url=url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
            # return {"lat": posts[0]['lat'], "lon": posts[0]['lon']}
        else:
            print('Error:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None


def get_weather(lat, lon, api_key, units="standard"):
    # Define the API endpoint URL
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': units,
    }

    try:
        # Make a GET request to the API endpoint using requests.get()
        response = requests.get(url=url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        # Handle any network-related errors or exceptions
        print('Error:', e)
        return None


def main():
    # city = str(input('Enter the city name: '))
    city = "London"
    api_key = OPEN_WEATHER_API_KEY
    temp_units = 'metric'

    coords = get_city_coords(city=city, api_key=api_key)
    if coords:
        # json_coords = json.dumps(coords, indent=4, ensure_ascii=False)
        # print(json_coords)

        # for val in coords:
        #     name, country, state = val['name'], val['country'], val['state']
        #     print(f'Name: {name}, country: {country}, state: {state}')

        weather_obj = get_weather(
            lat=coords['lat'],
            lon=coords['lon'],
            api_key=api_key,
            units=temp_units,
        )
        if weather_obj:
            json_str = json.dumps(weather_obj, indent=4)
            print(json_str)

            # print('Temperature:', weather_obj['main']['temp'])
            # print('Feels like:', weather_obj['main']['feels_like'])
        else:
            print(f'Failed to get weather info for {city}')
    else:
        print(f'Failed to get coords for {city}!\nTry another time.')


if __name__ == '__main__':
    main()
