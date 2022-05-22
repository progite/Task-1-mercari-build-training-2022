import logging
from unicodedata import category, name
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from importlib_metadata import method_cache
from pydantic import BaseModel
import json
import database
import random

from requests import request
from sqlalchemy import union


class Item(BaseModel):
    name: str
    category: str
    image : str

app = FastAPI()
logger = logging.getLogger("uvicorn")
logger.level = logging.INFO
dict_items = {"items": []}


@app.get("/")
def root():
    return {"message": "Hello World!"}


@app.post("/items")
async def add_item(item: Item):
    id = random.randint(0, 10**6)
    database.insert_values(id, item.name, item.category, item.image)
    # dict_items["items"].append({"name" : str(item.name),"category": str(item.category)})
    # with open("items.json","w") as file:
    #     json.dump(dict_items,file)
    return {"message": f"item received: {item.name},{item.image}"}


@app.get("/items")
async def get_items():
    database.display_db()
    return
    with open("items.json", "r") as file:
        items = json.load(file)
        return json.dumps(items)


@app.get("/search/")
def get_keyword(name: str):  # will search for items with name = keyword given
    print("Debug")
    ans = database.search_keyword(name)
    return ans