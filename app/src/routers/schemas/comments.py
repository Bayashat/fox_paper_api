from datetime import datetime
from pydantic import BaseModel


class CommentResponse(BaseModel):
    id: int
    content: str
    created_at: datetime
    updated_at: datetime
    user_id: int
    research_id: int
    

class CommentCreateRequest(BaseModel):
    content: str

