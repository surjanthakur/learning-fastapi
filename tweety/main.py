import select
from fastapi import FastAPI, HTTPException, status, Depends
from contextlib import asynccontextmanager
from database import create_db_and_tables, get_session
from sqlmodel import Session
from sql_model import User, Tweet
from pydantic_schema import pydantic_tweet, pydantic_user
from fastapi.responses import JSONResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        create_db_and_tables()
        print("databse connection is created 🔻")
        yield
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err)
        )


app = FastAPI(lifespan=lifespan)


# get all tweets
@app.get("/tweets")
def get_all_tweets(db: Session = Depends(get_session)):
    all_tweets = db.exec(select(Tweet)).all()
    return all_tweets


# create new user
@app.post("/users/create")
def create_users(user_data: pydantic_user, db: Session = Depends(get_session)):
    new_user = User(name=user_data.name, email=user_data.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=f"user: {new_user.email} created successfullt !!",
    )
