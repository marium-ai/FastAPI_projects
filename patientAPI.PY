from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open("patient.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"Message": "A fully functional API to manage your patient records"}


@app.get("/view")
def view():
    data = load_data()
    return data


@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description="ID of the patient in the DB", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")


# 🚀 NEW: Sorting endpoint
@app.get("/sort")
def sort_patients(
    by: str = Query(..., description="Field to sort by (age, weight, name, etc.)"),
    order: str = Query("asc", description="Sort order: asc or desc")
):
    """
    Sort patients by any numeric or string field.
    Example: /sort?by=age&order=desc
    """
    data = load_data()

    # agar data dict hai (P001: {...}), list me convert karo
    if isinstance(data, dict):
        patients = list(data.values())
    else:
        patients = data

    # check field exists
    if not patients or by not in patients[0]:
        raise HTTPException(status_code=400, detail=f"Field '{by}' not found in patient data")

    reverse = True if order.lower() == "desc" else False

    try:
        # safe sort: handle None/missing values
        sorted_data = sorted(
            patients,
            key=lambda x: (x.get(by) is None, x.get(by)),
            reverse=reverse
        )
    except TypeError:
        # fallback if mix of str/int values
        sorted_data = sorted(
            patients,
            key=lambda x: str(x.get(by)).lower() if x.get(by) is not None else "",
            reverse=reverse
        )

    return sorted_data
