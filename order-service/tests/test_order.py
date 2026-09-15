from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json()["service"] == "order-service"


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json()["status"] == "UP"


def test_create_order():

    order = {
        "product_id": 100,
        "quantity": 2,
        "customer_id": 10
    }

    response = client.post(
        "/orders",
        json=order
    )

    assert response.status_code == 200

    data = response.json()

    assert data["product_id"] == 100
    assert data["quantity"] == 2
    assert data["status"] == "CREATED"