import requests

def get_echo():
    response = requests.get("https://postman-echo.com/get?foo=bar")
    return response
