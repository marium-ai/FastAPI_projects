from fastapi import FastAPI

app = FastAPI()

# Fixed rate (example)
RATE = 278

@app.get("/")
def home():
    return {"message": "Welcome to Simple PKR ↔ USD Converter 💱"}

@app.get("/pkr-to-usd/{amount}")
def pkr_to_usd(amount: float):
    return {
        "from": "PKR",
        "to": "USD",
        "amount": amount,
        "converted_amount": round(amount / RATE, 2)
    }

@app.get("/usd-to-pkr/{amount}")
def usd_to_pkr(amount: float):
    return {
        "from": "USD",
        "to": "PKR",
        "amount": amount,
        "converted_amount": round(amount * RATE, 2)
    }
