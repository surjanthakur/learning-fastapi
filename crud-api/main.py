from fastapi import FastAPI
import json

app = FastAPI()


# load data function.
def load_data():
    with open("patient.json", "r") as data:
        result = json.load(data)
    return result


@app.get("/all-patient")
def get_allPatients():
    data = load_data()
    return {f"all-patients: {data}"}
