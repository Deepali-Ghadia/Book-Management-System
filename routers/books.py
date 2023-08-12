from fastapi import APIRouter, status, HTTPException
from database import db
import schemas
import models
import sqlalchemy


router = APIRouter(prefix="/books", tags=["Books"])


# view list of all the books
@router.get('/list_all', status_code = status.HTTP_200_OK)
def get_all_books():
        books = db.query(models.Book).all()
        
        if not books:
                raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="There are no books in the database")
        return books



# add book to the database
@router.post("/add_new", response_model=schemas.ShowBook)
def add_book(book: schemas.AddBook):
        
        # check whether the book already exists or not
        is_present = db.query(models.Book).filter(models.Book.isbn_number == book.isbn_number).first()
        
        if is_present:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Book with same ISBN number already exists in the database")
        
        # ISBN number is of 13 digits, therefore need to validate 
        if len(str(book.isbn_number)) != 13:
                raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Enter ISBN number of valid length")
        
        new_book = models.Book(
                name = book.name,
                language = book.language,
                author = book.author,
                price = book.price,
                isbn_number = book.isbn_number
        )
        
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book



# update details of the book
@router.put("/update/{id}")
def update_details_of_a_book(id: int, book:schemas.UpdateBook):
        book_details = db.query(models.Book).filter(models.Book.id == id).first()    
        
        if not book_details:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No record for book with this id exists")
        book_details.name = book.name
        book_details.language = book.language
        book_details.author = book.author
        book_details.price = book.price
        
        db.commit()
        db.refresh(book_details)
        return book_details
        
    
    
@router.delete('/delete/{id}')
def delete_a_book(id: int):
    book_to_delete = db.query(models.Book).filter(models.Book.id==id).first()
    
    if book_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No record for book with this id exists")
    
    try:
        db.delete(book_to_delete)
        db.commit()
        db.refresh(book_to_delete)
        
    except sqlalchemy.exc.InvalidRequestError:
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Book deleted successfully")