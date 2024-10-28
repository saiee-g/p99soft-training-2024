from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

@app.get('/')
def read():
    return {"hello":"world"}

@app.get('/items/{item_id}')
def item_list(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q":q}

@app.put("/items/{item_id}")
def update_item_list(item_id: int, item: Item):
    return{"item_name": item.name, "item_id":item_id}