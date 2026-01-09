from pydantic import BaseModel, EmailStr, Field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):
    name: Annotated[
        str,
        Field(
            min_length=3,
            max_length=50,
            title="name of the patient",
            description="add name in less then 50 characters",
            examples=["amit", "roy"],
        ),
    ]
    email: EmailStr
    weight: float = Field(gt=0)
    age: int = Field(gt=0, lt=100)
    gender: str = Field(min_length=4, max_length=7)
    blood_group: str = Field(min_length=1, max_length=3)
    disease: Optional[List[str]] = (
        None  # when you add optional add default value [None]
    )
    admitted: bool
    contact_details: Dict[str, str]
