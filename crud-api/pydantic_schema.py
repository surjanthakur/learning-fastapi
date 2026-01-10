from pydantic import BaseModel, EmailStr, Field, computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    id: str
    name: str
    email: EmailStr
    weight: float
    age: int
    gender: str
    blood_group: str
    disease: Optional[List[str]] = None
    admitted: bool


@computed_field
@property
def bmi(self) -> float:
    bmi = round(self.weight / (self.height**2), 2)
    return bmi
