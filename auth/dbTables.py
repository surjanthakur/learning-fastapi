# Database table definitions for authentication and notes management
from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional
from uuid import uuid4


# Function to generate unique IDs ------------------------------------------------------->
def generate_id() -> str:
    return str(uuid4())


# Table for storing users --------------------------------------------------------------->
class User(SQLModel, table=True):
    id: str = Field(default_factory=generate_id)
    username: str = Field(min_length=3, max_length=50, unique=True)
    email: str = Field(primary_key=True, min_length=4, max_length=100, unique=True)
    password: str = Field(min_length=3, max_length=200)

    notes: List["Notes"] = Relationship(
        back_populates="owner",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "passive_deletes": True,
        },
    )


# Table for storing notes --------------------------------------------------------------->
class Notes(SQLModel, table=True):
    id: str = Field(primary_key=True, default_factory=generate_id)
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=5, max_length=20000)

    owner_email: str = Field(default=None, foreign_key="user.email", nullable=True)
    owner: Optional["User"] = Relationship(
        back_populates="notes",
    )
