from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import datetime, date
from typing import Optional

from ...models.id_abc import Gender, UserRole

class UserModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    password: str 
    gender: str 
    phone_number: PhoneNumber | None
    date_of_birth: date | None
    biography: str | None
    created_at: datetime
    updated_at: datetime
    role_id: int


class SignupSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    gender: Gender | None
    phone_number: PhoneNumber | None
    date_of_birth: date | None = None
    
    
class LoginSchema(BaseModel):
    email: EmailStr
    password: str
    
    
    
class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    password: str | None = None
    gender: Gender | None = None
    phone_number: PhoneNumber | None = None
    date_of_birth: date | None = None
    biography: str | None = None
    role_id: int | None = None

