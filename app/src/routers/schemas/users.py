from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import datetime, date
from typing import Optional
from app.src.models.id_abc import Gender, UserRole

class UserModel(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    password: str 
    gender: str 
    phone_number: PhoneNumber
    date_of_birth: date
    biography: str
    created_at: datetime
    updated_at: datetime
    role_id: int


class SignupSchema(BaseModel):
    first_name: str = "admin"
    last_name: str = "adminovich"
    email: EmailStr = "admin@gmail.com"
    password: str = "admin"
    gender: Gender | None
    phone_number: PhoneNumber | None = "+77078788885"
    date_of_birth: Optional[date] 
    biography: Optional[str]
    
    
class LoginSchema(BaseModel):
    email: EmailStr = "admin@gmail.com"
    password: str = "admin"
    
class ProfileSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    gender: Optional[str]
    phone_number: Optional[PhoneNumber]
    date_of_birth: Optional[date] 
    biography: Optional[str]
    created_at: datetime
    updated_at: datetime
    role_id: int

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    gender: Optional[str] = None
    phone_number: Optional[PhoneNumber] = None
    date_of_birth: Optional[date] = None
    biography: Optional[str] = None
    role_id: Optional[int] = None
    
class UserResponse(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    gender: Optional[str] = None
    phone_number: Optional[PhoneNumber] = None
    date_of_birth: Optional[date] = None
    biography: Optional[str] = None
    role_id: Optional[int] = None
    
    
class UserCreate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    gender: Optional[str] = None
    phone_number: Optional[PhoneNumber] = None
    date_of_birth: Optional[date] = None
    biography: Optional[str] = None
    role_id: Optional[int] = None
    
