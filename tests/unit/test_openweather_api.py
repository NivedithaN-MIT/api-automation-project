import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from apis.openweather_api import OpenWeatherAPI
import unittest
from unittest.mock import patch


class TestOpenWeatherAPI(unittest.TestCase):

    @patch('apis.openweather_api.requests.get')
    def test_get_weather_by_city(self, mock_get):
        # Mock response data
        mock_response = {
            "weather": [{"description": "clear sky"}],
            "main": {"temp": 30.5}
        }

        # Configure the mock to return a response with .json() method
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response

        api = OpenWeatherAPI("fake_api_key")
        result = api.get_weather_by_city("Chennai")

        # Assertions
        self.assertEqual(result["weather"][0]["description"], "clear sky")
        self.assertEqual(result["main"]["temp"], 30.5)

if __name__ == '__main__':
    unittest.main()