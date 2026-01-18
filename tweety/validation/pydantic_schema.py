from pydantic import BaseModel, EmailStr, Field, field_validator


class pydantic_user(BaseModel):
    name: str = Field(min_length=3, max_length=20)
    email: EmailStr = Field(unique=True)

    @field_validator("email", mode="before")
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["gmail.com"]
        domain_name = value.split("@")[-1]
        if domain_name not in valid_domains:
            raise ValueError("opps! not a valid gmail.")
        return value

    @field_validator("name", mode="after")
    @classmethod
    def name_validator(cls, value):
        return value.capitalize()


class pydantic_tweet(BaseModel):
    content: str = Field(min_length=10, max_length=400)

    @field_validator("content", mode="after")
    @classmethod
    def transform_content(cls, value):
        return value.title()
