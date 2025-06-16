import os
from dotenv import load_dotenv
from apis.openweathermap import OpenWeatherAPI

load_dotenv()

def test_weather_api():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    assert api_key, "OPENWEATHER_API_KEY not set in environment"

    weather_api = OpenWeatherAPI(api_key)
    response = weather_api.get_weather("London")

    assert response.status_code == 200
    data = response.json()
    assert "weather" in data
    assert "main" in data
