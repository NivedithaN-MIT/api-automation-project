from dotenv import load_dotenv
import os
from apis.openweathermap import OpenWeatherAPI

# Load environment variables from .env
load_dotenv()


def test_weather_api():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    assert api_key is not None, "OPENWEATHER_API_KEY not set in environment"

    weather_api = OpenWeatherAPI(api_key)
    response = weather_api.get_weather("London")

    assert response.status_code == 200, "API call failed"

    data = response.json()
    assert "weather" in data, "'weather' key missing in response"
    assert "main" in data, "'main' key missing in response"
