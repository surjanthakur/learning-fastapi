from pydantic import BaseModel, EmailStr


class InputNotes(BaseModel):
    owner: EmailStr
    title: str
    content: str


class ShowNotes(BaseModel):
    title: str
    content: str
