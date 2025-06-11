from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class CommentBase(BaseModel):
    text: str = Field(..., min_length=1, max_length=500)
    advertisement_id: int


class CommentCreate(CommentBase):
    pass


class CommentRead(CommentBase):
    id: int
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class CommentUpdate(BaseModel):
    text: str = Field(..., min_length=1, max_length=500)
