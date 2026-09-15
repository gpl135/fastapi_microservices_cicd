from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List


app = FastAPI(
    title="Order Service",
    version="1.0.0"
)


class Order(BaseModel):
    product_id: int
    quantity: int
    customer_id: int


orders = []


@app.get("/")
def root():
    return {
        "service": "order-service",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.post("/orders")
def create_order(order: Order):

    order_id = len(orders) + 1

    new_order = {
        "order_id": order_id,
        "product_id": order.product_id,
        "quantity": order.quantity,
        "customer_id": order.customer_id,
        "status": "CREATED"
    }

    orders.append(new_order)

    return new_order


@app.get("/orders")
def get_orders() -> List[dict]:

    return orders


@app.get("/orders/{order_id}")
def get_order(order_id: int):

    for order in orders:

        if order["order_id"] == order_id:
            return order

    raise HTTPException(
        status_code=404,
        detail="Order not found"
    )