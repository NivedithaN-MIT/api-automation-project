import requests

def get_posts():
    return requests.get("https://jsonplaceholder.typicode.com/posts")
