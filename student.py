from fastapi import FastAPI,Path
import json

app = FastAPI()

def load_data():
    with open("class.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/welcome")
def welcome():
    return {"message": "welcome to ABC school student's info"}

@app.get("/info")
def info():
    data = load_data()
    return data

@app.get("/student/{student_id}")
def view_studentid(student_id: str):
    data = load_data()
    if student_id in data:
        return data[student_id]
    return {"error": "Student not found"}
