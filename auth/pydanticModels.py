from pydantic import BaseModel, EmailStr


class ShowNotes(BaseModel):
    title: str
    content: str


class ShowUser(BaseModel):
    username: str
    email: EmailStr
