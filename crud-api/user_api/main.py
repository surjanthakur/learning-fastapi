from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
import json
from pydantic_schema import User

app = FastAPI()


def load_data():
    with open("users.json", "r") as file:
        data = json.load(file)
    return data


def save_data(data):
    with open("users.json", "w") as file:
        json.dump(data, file)


# get all users
@app.get("/users")
def get_all_users():
    try:
        data = load_data()
        return JSONResponse(status_code=status.HTTP_200_OK, content=data)
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)


# create new user
@app.post("/users/create")
def create_user(user_data: User):
    data = load_data()

    if user_data.id in data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="enter valid id this might be wrong !!",
        )
    data[user_data.id] = user_data.model_dump(exclude=["id"])
    save_data(data=data)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=f"user {user_data.name} created successfully",
    )
