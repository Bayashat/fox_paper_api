from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import date
from typing import Optional

class CreateUser(BaseModel):
    first_name: str = "admin"
    last_name: str = "adminovich"
    email: EmailStr = "admin@gmail.com"
    password: str = "admin"
    gender: Optional[int] = 0
    phone_number: PhoneNumber = "+77051985048"
    date_of_birth: Optional[date] 
    biography: Optional[str]
    # role_id: int
    
    