from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings

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
    return settings.STRIPE_KEY


