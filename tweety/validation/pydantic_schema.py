from pydantic import BaseModel, EmailStr, Field
from typing import List


class pydantic_user(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    email: EmailStr = Field(unique=True)


class pydantic_tweet(BaseModel):
    content: str = Field(min_length=10, max_length=400)
