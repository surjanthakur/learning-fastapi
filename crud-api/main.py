from fastapi import FastAPI, Path, HTTPException, status, Query
import json

app = FastAPI()


# load data function.
def load_data():
    with open("patient.json", "r") as data:
        result = json.load(data)
    return result


@app.get("/patients")
def get_all_patients():
    data = load_data()
    return {f"all-patients: {data}"}


@app.get("/patients/{id}")
def get_patient_by_id(
    id: str = Path(
        ...,
        description="this api gives you patient data based on their id",
        max_length=6,
        min_length=4,
        example="p001",
    )
):
    response = load_data()
    if id in response:
        return response[id]
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="opps!👻 patient not fount 404",
        )


@app.post("/patients/create")
def create_patient():
    pass
