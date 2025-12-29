from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200

def test_create_task_api():
    response = client.post(
        "/api/tasks",
        json={"title": "Test Task", "description": "Testing API", "status": False},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert "id" in data

def test_read_tasks_api():
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)