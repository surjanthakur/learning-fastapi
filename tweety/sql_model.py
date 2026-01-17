from pydantic import EmailStr
import datetime
from sqlmodel import Field, Session, SQLModel, create_engine, select, table, true


class User(SQLModel, table=True):
    id: str = Field(primary_key=True, default=None)
    name: str = Field(min_length=3, max_length=20)
    email: EmailStr = Field(unique=True)
    created_at: str = Field(default=datetime.date.today())
    updated_at: str = Field(default=datetime.date.today())


class Tweet(SQLModel, table=True):
    id: str = Field(primary_key=True, default=None)
    content: str = Field(min_length=10, max_length=400)
    created_at: str = Field(default=datetime.date.today())
    updated_at: str = Field(default=datetime.date.today())
