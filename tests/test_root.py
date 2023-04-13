import requests

from confest import BASE_URL

def test_root():
    response = requests.get(BASE_URL)
    
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World from Todo API"}