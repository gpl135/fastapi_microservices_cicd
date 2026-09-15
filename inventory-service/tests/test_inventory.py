from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["service"] == "inventory-service"


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "UP"


def test_get_inventory():

    response = client.get("/inventory/100")

    assert response.status_code == 200

    data = response.json()

    assert data["product_id"] == 100
    assert data["quantity"] == 50


def test_update_inventory():

    item = {
        "product_id": 100,
        "quantity": 75
    }

    response = client.post(
        "/inventory",
        json=item
    )

    assert response.status_code == 200

    data = response.json()

    assert data["quantity"] == 75
    assert data["status"] == "UPDATED"