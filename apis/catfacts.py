import requests

def get_cat_fact():
    return requests.get("https://catfact.ninja/fact")
