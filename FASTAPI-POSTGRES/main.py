from fastapi import FastAPI, Depends, HTTPException
import services, models, schemas
from db import get_db, engine
from sqlalchemy.orm import Session

from typing import List as list

app = FastAPI()

@app.get("/books/", response_model=list[schemas.Book])
async def get_all_books(db: Session = Depends(get_db)):
    return services.get_books(db)

@app.get("/books/{id}", response_model=schemas.Book)
async def get_book_by_id(id: int, db: Session = Depends(get_db)):
    book_queryset = services.get_book(db, id) 
    if book_queryset:
        return book_queryset
    raise HTTPException(status_code = 404, detail = "Invalid book id provided.")

@app.post("/books/", response_model=schemas.Book)
async def create_new_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create_book(db, book)


