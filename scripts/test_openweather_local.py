import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from apis.openweather_api import OpenWeatherAPI

api_key = "00d4ab8161fd8da9b09a1157796429dd"  # Replace with your real key
weather_api = OpenWeatherAPI(api_key)

city = "Chennai"
data = weather_api.get_weather_by_city(city)

print(f"Weather in {city}: {data['weather'][0]['description']}, Temp: {data['main']['temp']}°C")
