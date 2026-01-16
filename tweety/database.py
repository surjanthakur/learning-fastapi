# This file handles database setup, connection and session management for the Tweety app.

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, SQLModel, create_engine, select
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")
print(DB_URL)

engine = create_engine(DB_URL)


# create the database and tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# get the session for the database on per request.
def get_session():
    with Session(engine) as session:
        yield session
