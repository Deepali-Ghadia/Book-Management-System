from database import Base
from sqlalchemy import Column, Integer, String, BIGINT


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    language = Column(String, nullable=False)
    author = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    isbn_number = Column(BIGINT, nullable=False, unique=True)
    