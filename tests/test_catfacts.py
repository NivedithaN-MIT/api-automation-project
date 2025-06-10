from apis.catfacts import get_cat_fact

def test_cat_fact():
    response = get_cat_fact()
    assert response.status_code == 200
    assert "fact" in response.json()
