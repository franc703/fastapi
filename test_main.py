from fastapi.testclient import TestClient
import main

client = TestClient(main.app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello Duke"}


def test_add():
    num1 = 5
    num2 = 10
    response = client.get(f"/add/{num1}/{num2}")
    assert response.status_code == 200
    assert response.json() == {"total": num1 + num2}
