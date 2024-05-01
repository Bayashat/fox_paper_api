from pydantic import BaseModel


class ResearchSchema(BaseModel):
    id: int
    title: str
    description: str
    author_id: int

class FavoriteSchema(BaseModel):
    id: int
    research: ResearchSchema

    class Config:
        orm_mode = True