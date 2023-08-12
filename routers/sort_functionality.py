from fastapi import APIRouter
from database import db
import models




router = APIRouter(prefix="/books", tags=["Sort Functionality"])

@router.get("/sort/{order}")
def sort_books_in_descending_order_based_on_price(order: str):
    
    if order == "desc":
        books = db.query(models.Book).order_by(models.Book.price.desc()).all()
        
    if order == "asc":
        books = db.query(models.Book).order_by(models.Book.price).all()
        
    return books