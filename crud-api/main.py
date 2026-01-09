from fastapi import FastAPI, Path, HTTPException, status, Query
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


@app.get("/sort")
def sort_patient(
    sort_by: str = Query(..., description="sort by based on: weight,height,bmi"),
    order: str = Query("asc", description="sort in asc. or desc. order"),
):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="provided field is wrong enter valide data pls.🙏🏻",
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="provided field is wrong enter valide data pls.🙏🏻",
        )

    data = load_data()
    sort_order = True if order == "desc" else False

    sorted_data = sorted(
        data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order
    )

    return sorted_data
