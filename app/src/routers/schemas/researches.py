from pydantic import BaseModel
from datetime import datetime

from ...models.id_abc import Status


class ResearchResponse(BaseModel):
    id: int
    title: str
    description: str
    status: Status
    is_published: bool
    file_id: int
    created_at: datetime
    updated_at: datetime
    published_at: datetime | None = None
    author_id: str
    category_ids: str
    

class ResearchCreateRequest(BaseModel):
    title: str
    description: str
    file_id: int
    category_ids: str
    

class ResearchUpdateRequest(BaseModel):
    title: str = None
    description: str = None
    file_id: int = None
    category_ids: str = None