from pydantic import BaseModel

from app.src.routers.schemas.users import UserModel

class AuthResponse(BaseModel):
    access_token: str
    user: UserModel