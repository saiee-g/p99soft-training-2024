from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    id: int
    price: float
    tax: float | None = None

@app.get("/")
def hello():
    return "HI"
    
@app.get("/items")
def show_items(item: Item):
    return item
    
@app.post("/items/")
def total_price(item: Item):
    item_dict = item.dict()
    if item.tax:
        item_price = item.price + item.tax
        item_dict.update({"Total price": item_price})
    return item_dict

@app.get("/items/{item_id}")
def ask_item(item_id: int, saiee: str|None = None, intq: int|None = None):
    return{"item_id": item_id, "query":saiee , "intq": intq}