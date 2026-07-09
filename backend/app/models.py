```python
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    genre = Column(String(100), nullable=True)
    status = Column(String(20), nullable=False, default="wishlist")
    rating = Column(Integer, nullable=True)
    total_pages = Column(Integer, nullable=True)
    current_page = Column(Integer, default=0)
    notes = Column(Text, nullable=True)
    cover_color = Column(String(7), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    started_at = Column(DateTime, nullable=True)
    finished_at = Column(DateTime, nullable=True)


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    phone = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
```

## FILE: backend/app/schemas.py
```python
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


class CustomerOut(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
```

## FILE: backend/app/database.py
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./book_tracker.db"

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

## FILE: backend/app/main.py
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import books, customers

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(books.router)
app.include_router(customers.router)
```

## FILE: backend/app/routers/customers.py
```python
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Customer
from ..schemas import CustomerOut

router = APIRouter(prefix="/customers", tags=["customers"])


@router.get("/{customer_id}", response_model=CustomerOut, status_code=200)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == customer_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
```