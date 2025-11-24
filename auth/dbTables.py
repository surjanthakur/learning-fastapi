# Database table definitions for authentication and notes management

from sqlmodel import Field, SQLModel, Relationship
from typing import List

# Define the database tables using SQLModel


# Table for storing owner notes
class OwnerNotes(SQLModel, table=True):
    id: str = Field(primary_key=True, default=None)
    name: str = Field(min_length=1, max_length=100)
    notes: List["Notes"] = Relationship(back_populates="owner")


# Table for storing notes
class Notes(SQLModel, table=True):
    id: str = Field(primary_key=True, default=None)
    user_id: str = Field(foreign_key="OwnerNotes.id")
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=5, max_length=20000)
    owner: OwnerNotes = Relationship(back_populates="notes")


# Table for storing authentication user information
class Users(SQLModel, table=True):
    id: str = Field(primary_key=True, default=True)
    username: str = Field(min_length=3, max_length=50, unique=True)
    email: str = Field(min_length=4, max_length=100, unique=True)
    password: str = Field(min_length=3, max_length=200)
