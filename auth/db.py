from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv("DB_URL")

engine = create_engine(database_url)


# create the database and tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("Database and tables created.👍")


# Dependency to get DB session
def get_session():
    with Session(engine) as session:
        yield session
