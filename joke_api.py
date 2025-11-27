from fastapi import FastAPI
import random

app = FastAPI()

jokes = [
    "Why don't programmers like nature? It has too many bugs.",
    "I told my computer I needed a break… now it won’t stop sending me KitKats.",
    "Debugging: Being the detective in a crime movie where you're also the murderer.",
    "Why did the developer go broke? Because he used up all his cache."
]

@app.get("/joke")
def get_joke():
    return {"joke": random.choice(jokes)}
