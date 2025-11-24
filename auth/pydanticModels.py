from pydantic import BaseModel, EmailStr


class ShowNotes(BaseModel):
    title: str
    content: str
    owner_email: str
