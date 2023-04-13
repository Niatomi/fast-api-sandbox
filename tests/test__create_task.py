import requests
from confest import BASE_URL

def test_create_task_ok():
    response = requests.put(f'{BASE_URL}/create-task', json={
        "content": "string",
        "user_id": "string",
        "task_id": "string",
        "is_done": False
    })
    
    assert response.status_code == 200
    assert len(response.json()) == 1