from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Payment Service",
    version="1.0.0"
)


class Payment(BaseModel):
    order_id: int
    amount: float


payments = []


@app.get("/")
def root():

    return {
        "service": "payment-service",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "UP"
    }


@app.post("/payments")
def create_payment(payment: Payment):

    payment_id = len(payments) + 1

    new_payment = {
        "payment_id": payment_id,
        "order_id": payment.order_id,
        "amount": payment.amount,
        "status": "SUCCESS"
    }

    payments.append(new_payment)

    return new_payment


@app.get("/payments")
def get_payments():

    return payments