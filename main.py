from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Welcome to FastAPI"

@app.get("/contact")
def contact():
    return "Contact Us anytime you want, Thank you!"