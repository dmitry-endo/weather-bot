import json
import requests


def get_posts():
    # url = 'https://jsonplaceholder.typicode.com/posts'
    # \?latitude=55.7522&longitude=37.6156&hourly=temperature_2m,rain,showers,snowfall&timezone=Europe%2FMoscow&forecast_days=1
    url = 'https://api.open-meteo.com/v1/forecast'

    params = {
        'latitude': 55.7522,
        'longitude': 37.6156,
        'hourly': ['temperature_2m', 'rain'],
        'timezone': 'auto',
        'forecast_days': 1,
    }

    try:
        response = requests.get(url=url, params=params)

        if response.status_code == 200:
            posts = response.json()
            return posts
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def main():
    posts = get_posts()

    if posts:
        # print('First Post Title:', posts[0]['title'])
        # print('First Post Body:', posts[0]['body'])
        # print(posts)
        json_str = json.dumps(posts, indent=4)
        print(json_str)
    else:
        print('Failed to fetch posts from API.')


if __name__ == '__main__':
    main()
