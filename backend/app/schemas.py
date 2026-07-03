from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Literal
from datetime import datetime


class BookCreate(BaseModel):
    title: str
    author: str
    genre: Optional[str] = None
    status: Literal["wishlist", "reading", "finished"] = "wishlist"
    rating: Optional[int] = Field(None, ge=1, le=5)
    total_pages: Optional[int] = None
    notes: Optional[str] = None
    cover_color: Optional[str] = None


class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    genre: Optional[str] = None
    status: Optional[Literal["wishlist", "reading", "finished"]] = None
    rating: Optional[int] = Field(None, ge=1, le=5)
    total_pages: Optional[int] = None
    notes: Optional[str] = None
    cover_color: Optional[str] = None


class BookOut(BaseModel):
    id: int
    title: str
    author: str
    genre: Optional[str]
    status: str
    rating: Optional[int]
    total_pages: Optional[int]
    current_page: int
    notes: Optional[str]
    cover_color: Optional[str]
    created_at: datetime
    updated_at: datetime
    started_at: Optional[datetime]
    finished_at: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)
