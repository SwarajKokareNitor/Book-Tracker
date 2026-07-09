```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## FILE: backend/app/models.py
```python
from sqlalchemy import Column, Integer, String
from app.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, nullable=False)
    published_year = Column(Integer, nullable=False)
    status = Column(String, nullable=False)
```

## FILE: backend/app/schemas.py
```python
from pydantic import BaseModel


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    published_year: int
    status: str

    class Config:
        from_attributes = True
```

## FILE: backend/app/repositories/book_repository.py
```python
from sqlalchemy.orm import Session
from app.models import Book
from typing import Optional


class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_book_by_id(self, book_id: int) -> Optional[Book]:
        return self.db.query(Book).filter(Book.id == book_id).first()
```

## FILE: backend/app/routers/books.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import BookResponse
from app.repositories.book_repository import BookRepository

router = APIRouter()


@router.get("/books/{book_id}", response_model=BookResponse, status_code=200)
def get_book(book_id: int, db: Session = Depends(get_db)):
    repository = BookRepository(db)
    book = repository.get_book_by_id(book_id)
    
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book
```

## FILE: backend/app/main.py
```python
from fastapi import FastAPI
from app.database import engine, Base
from app.routers import books

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Book Details API")

app.include_router(books.router)
```