from fastapi import FastAPI, HTTPException
from dbConnection import create_db_and_tables
from contextlib import asynccontextmanager
from router import notes, auth


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database and create tables when the app starts
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)

# Include the notes router
app.include_router(notes.router)
app.include_router(auth.router)
