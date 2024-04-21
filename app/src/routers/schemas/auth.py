from pydantic import BaseModel
from ..schemas.users import UserModel

class AuthResponse(BaseModel):
    access_token: str
    user: UserModel