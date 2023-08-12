from fastapi import APIRouter, status, HTTPException
from database import db
import models


# books can be filtered on the basis of language, price range, author

router = APIRouter(prefix="/books", tags=["Filter Functionality"])

@router.get("/filter/")
def filter_books(language: str = None, min_price: int = None, max_price: int = None):
    
    results = []
    books = db.query(models.Book).all()
    
    if language:
        for book in books:
            if book.language.lower() == language.lower():
                results.append(book)
                
        if not results:
            raise(HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail = "There are no books written in this language"))
        
        
    if min_price:
        for book in books:
            if book.price > min_price:
                results.append(book)
                
        if not results:
            raise(HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail = "There are no books having price greater than this amount"))
        
    if max_price:
        for book in books:
            if book.price < max_price:
                results.append(book)
                
        if not results:
            raise(HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail = "There are no books having price less than this amount"))
    
    results = set(results)
        
    return {"results" :  results}