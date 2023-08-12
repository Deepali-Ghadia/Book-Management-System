from pydantic import BaseModel


class ShowBook(BaseModel):
    id: int
    name: str
    language: str
    author: str
    price: int
    isbn_number: int
    
    class Config:
        orm_mode = True
        
        
class AddBook(BaseModel):
    name: str
    language: str
    author: str
    price: int
    isbn_number: int
    
    class Config:
        orm_mode = True
        
        
class UpdateBook(BaseModel):
    name: str
    language: str
    author: str
    price: int
    
    class Config:
        orm_mode = True