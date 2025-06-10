import requests

def get_users():
    return requests.get("https://reqres.in/api/users?page=2")

def create_user(name, job):
    return requests.post("https://reqres.in/api/users", json={"name": name, "job": job})
