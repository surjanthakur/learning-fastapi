from fastapi import FastAPI, HTTPException
from dbConnection import create_db_and_tables
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database and create tables when the app starts
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
