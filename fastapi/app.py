from flask import Flask
from pydantic import BaseModel
from fastapi import FastAPI

class Book(BaseModel):
    book_id: int
    name: str
    author: str
    price: float

book1 = Book(1, "Harry Potter", "J K Rowling", 560.70)
book2 = Book(2, "Twilight", "S Meyer", 260.70)

app = FastAPI(__name__)

@app.get("/")
def welcome():
    return {"Message" : "Welcome to our Book Store"}
#returns body
@app.get('/{book_id}')
def display(book_id: int):
    return {"book_id": book_id, "name": name, "author":author, "price": "price" }


if __name__ == "__main__":
    app.run(debug = True)
    