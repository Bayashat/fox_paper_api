from pydantic import BaseModel
from datetime import datetime
from fastapi import File, UploadFile
from typing import Annotated

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
    published_at: datetime | None
    author_id: str
    category_ids: str
    

class ResearchCreateRequest(BaseModel):
    title: str
    description: str
    file_id: int = 1
    category_ids: str
    

class ResearchUpdateRequest(BaseModel):
    title: str = None
    description: str = None
    file_id: int = None