from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
import json

app = FastAPI()


def load_data():
    with open("users.json", "r") as file:
        data = json.load(file)
    return data


# get all users
@app.get("/users")
def get_all_users():
    try:
        data = load_data()
        return JSONResponse(status_code=status.HTTP_200_OK, content=data)
    except Exception as error:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
