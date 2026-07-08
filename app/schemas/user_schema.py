from pydantic import BaseModel, EmailStr, Field, field_validator
import re

class UserCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=4,
        max_length=20,
        pattern=r"^[A-Za-z]+$"
    )
    email: EmailStr
    password: str

    @field_validator("name")
    @classmethod
    def validate_name(cls, value: str):

        # Remove leading/trailing spaces
        value = value.strip()

        # Remove extra spaces between words
        value = " ".join(value.split())

        if not value.replace(" ", "").isalpha():
            raise ValueError("Name should contain only letters")

        return value


    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if len(value)<8:
            raise ValueError("Password must be at least 8 characters")
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain an uppercase letter")
        if not re.search(r"\d", value):
            raise ValueError("Password must contain a number")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain a lowercase letter")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
             raise ValueError("Password must contain a special character")
        
        return value
    



class UserResponse(BaseModel):
    id: int
    name:str
    email: EmailStr

    model_config={
        "from_attributes":True
    }
    
class UserLogin(BaseModel):
    email: EmailStr
    password: str