import requests

def get_weather(city, api_key):
    import requests
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key}
    return requests.get(base_url, params=params)
