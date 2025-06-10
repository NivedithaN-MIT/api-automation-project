from dotenv import load_dotenv
import os
from apis.openweathermap import get_weather

load_dotenv()  # Load values from .env

def test_weather_api():
    api_key = os.getenv("OPENWEATHER_API_KEY")
    assert api_key is not None, "OPENWEATHER_API_KEY not set in environment"

    response = get_weather("London", api_key)
    assert response.status_code == 200
    data = response.json()
    assert "weather" in data
    assert "main" in data
