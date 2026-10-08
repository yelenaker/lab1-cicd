from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_create_item():
    response = client.post(
        "/api/items",
        json={
            "name": "Test Item",
            "description": "Test description",
            "price": 100
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test Item"
    assert data["price"] == 100


def test_get_items():
    response = client.get("/api/items")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_item_not_found():
    response = client.get("/api/items/999999")

    assert response.status_code == 404