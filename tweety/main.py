from fastapi import FastAPI, HTTPException, status, Depends, Path
from contextlib import asynccontextmanager
from database import create_db_and_tables, get_session
from sqlmodel import Session, select
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


# get user by their id
@app.get("/users/{user_id}")
def get_user_by_id(
    user_id: str = Path(
        ...,
        title="enter user_id",
        description="enter the user id to access information !!",
    ),
    db: Session = Depends(get_session),
):
    statement = select(User).where(User.id == user_id)
    user = db.exec(statement)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="invalid user_id enter the valid user id !!",
        )
    return JSONResponse(status_code=status.HTTP_200_OK, content=user)


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
