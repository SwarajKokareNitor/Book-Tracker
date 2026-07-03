from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from ..database import get_db
from ..models import Book
from ..schemas import BookCreate, BookUpdate, BookOut

router = APIRouter(prefix="/books", tags=["books"])


@router.post("", response_model=BookOut, status_code=status.HTTP_201_CREATED)
def create_book(body: BookCreate, db: Session = Depends(get_db)):
    book_data = body.model_dump()
    
    if body.status == "reading":
        book_data["started_at"] = datetime.utcnow()
    elif body.status == "finished":
        book_data["started_at"] = datetime.utcnow()
        book_data["finished_at"] = datetime.utcnow()
    
    db_book = Book(**book_data)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@router.get("", response_model=List[BookOut])
def get_books(
    status: Optional[str] = None,
    genre: Optional[str] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Book)
    
    if status is not None:
        query = query.filter(Book.status == status)
    
    if genre is not None:
        query = query.filter(Book.genre == genre)
    
    if search is not None:
        query = query.filter(Book.title.ilike(f"%{search}%"))
    
    books = query.order_by(Book.created_at.desc()).all()
    return books


@router.get("/{id}", response_model=BookOut)
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.patch("/{id}", response_model=BookOut)
def update_book(id: int, body: BookUpdate, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    update_data = body.model_dump(exclude_unset=True)
    
    if "status" in update_data:
        if update_data["status"] == "reading" and book.started_at is None:
            update_data["started_at"] = datetime.utcnow()
        elif update_data["status"] == "finished" and book.finished_at is None:
            update_data["finished_at"] = datetime.utcnow()
    
    for key, value in update_data.items():
        setattr(book, key, value)
    
    db.commit()
    db.refresh(book)
    return book


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == id).first()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return None
