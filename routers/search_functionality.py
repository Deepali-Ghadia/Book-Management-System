from fastapi import APIRouter, status, HTTPException
from database import db
import models


# books can be searched on the basis of name, author_name, isbn number, 

router = APIRouter(prefix="/books", tags=["Search Functionality"])

@router.get("/search")
def search_books(name: str = None, author: str = None, isbn_number: int = None):
    
    books = db.query(models.Book).all()
    
    results = []
    
    if name:
        for book in books:
            if name.lower() in book.name.lower(): 
                results.append(book)
                
        if not results:
                raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No books found")    
           
            
    if author:
        for book in books:
            if author.lower() in book.author.lower():
                results.append(book)
                
        if not results:
                raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No books found")    
            
            
    if isbn_number:
        for book in books:
            if str(isbn_number) in str(book.isbn_number):
                results.append(book)
                
        if not results:
                raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No books found") 
            
            
    return {"results" :  results}  