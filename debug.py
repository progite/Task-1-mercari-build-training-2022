from typing import Union
import json
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()
dict_items = {"items" : []}

@app.post("/items/")
def create_item(item: Item):
    dict_items["items"].append(str(item))
    with open("items.json","w") as file:
        json.dump(dict_items,file)
    
    return item
