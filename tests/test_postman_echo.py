from apis.postman_echo import get_echo

def test_postman_echo():
    response = get_echo()
    assert response.status_code == 200
    assert "args" in response.json()
