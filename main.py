from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import stripe
from config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY


origins = ["*"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main():
    return "Hi"

@app.get('/public-key')
def get_public_key():
    return {"publishableKey": settings.STRIPE_PUBLISHABLE_KEY}

class Payment(BaseModel):
    amount: int
@app.post('/payment-sheet')
def payment_sheet(payment: Payment):
  print(payment)  
  paymentIntent = stripe.PaymentIntent.create(
    amount=payment.amount,
    currency='usd',
    automatic_payment_methods={
      'enabled': True,
    },
  )
  return {"paymentIntent": paymentIntent.client_secret,
                 "publishableKey": settings.STRIPE_PUBLISHABLE_KEY}


