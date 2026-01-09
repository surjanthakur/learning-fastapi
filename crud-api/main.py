from fastapi import FastAPI
from data_validation import Patient_data
import json

app = FastAPI()


# load data function.
def load_data():
    with open("patient.json", "r") as data:
        result = json.load(data)
    return result


@app.get("/all-patient")
def get_all_patients():
    data = load_data()
    return {f"all-patients: {data}"}


@app.get("/patient/{id}")
def get_patient_by_id(id: str):
    response = load_data()
    if id in response:
        return response[id]
    else:
        return {"cant find patient with this id!!"}
