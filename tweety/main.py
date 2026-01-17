from fastapi import FastAPI, HTTPException, status
from contextlib import asynccontextmanager
from database import create_db_and_tables


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
