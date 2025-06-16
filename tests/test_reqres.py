from apis.reqres import get_users, create_user
from unittest.mock import patch

@patch("apis.reqres.requests.get")
def test_reqres_get_users(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "data": [{"id": 1, "email": "niveditha.n@mastechdigital.com"}]
    }

    response = get_users()
    assert response.status_code == 200
    assert "data" in response.json()

@patch("apis.reqres.requests.post")
def test_reqres_create_user(mock_post):
    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = {
        "name": "Niveditha", "job": "QA"
    }

    response = create_user("Niveditha", "QA")
    assert response.status_code == 201
    assert response.json()["name"] == "Niveditha"
