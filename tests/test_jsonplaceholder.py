from apis.jsonplaceholder import get_posts

def test_jsonplaceholder_posts():
    response = get_posts()
    assert response.status_code == 200
    assert isinstance(response.json(), list)
