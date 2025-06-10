from apis.reqres import get_users, create_user

def test_reqres_get_users():
    response = get_users()
    assert response.status_code == 200
    assert "data" in response.json()

def test_reqres_create_user():
    response = create_user("Niveditha", "QA")
    assert response.status_code == 201
    assert response.json()["name"] == "Niveditha"
