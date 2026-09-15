from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Inventory Service",
    version="1.0.0"
)


class Inventory(BaseModel):
    product_id: int
    quantity: int


inventory = {
    100: 50,
    101: 100,
    102: 25
}


@app.get("/")
def root():

    return {
        "service": "inventory-service",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "UP"
    }


@app.get("/inventory/{product_id}")
def get_inventory(product_id: int):

    quantity = inventory.get(product_id, 0)

    return {
        "product_id": product_id,
        "quantity": quantity
    }


@app.post("/inventory")
def update_inventory(item: Inventory):

    inventory[item.product_id] = item.quantity

    return {
        "product_id": item.product_id,
        "quantity": item.quantity,
        "status": "UPDATED"
    }