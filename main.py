from fastapi import FastAPI
from mockdata import products

app = FastAPI()


@app.get("/")
def home():
    return "Welcome to FastAPI"


@app.get("/contact")
def contact():
    return "Contact Us anytime you want, Thank you!"


@app.get("/products")
def get_products():
    return products