from fastapi import FastAPI
from routers import books, filter_functionality, search_functionality, sort_functionality

 
app = FastAPI()

app.include_router(books.router)
app.include_router(filter_functionality.router)
app.include_router(search_functionality.router)
app.include_router(sort_functionality.router)