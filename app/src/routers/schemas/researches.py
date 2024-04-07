from pydantic import BaseModel
from typing import Optional
from datetime import datetime



# for get_researches as response

class ResearchesRequest(BaseModel):
    id: int
    title: str
    description: str
    status: int
    is_published: bool
    file_id: int
    created_at: datetime
    updated_at: datetime
    published_at: datetime