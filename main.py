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

from image_encryption import hash_func


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
    encrypted_image_filename = hash_func(item.image)
    database.insert_values(id, item.name, item.category, encrypted_image_filename)
    
    return {"message": f"item received: {item.name}"}


@app.get("/items") #display_entire_database
async def get_items():
    database.display_db()

@app.get("/items/") #search_item_by_id [item_id = query_param]
async def get_item_details(item_id : str):
    print(item_id)
    return database.get_item_by_id(int(item_id))

@app.get("/search/") #search for all items with name = given keyword [keyword = query param]
def get_keyword(keyword: str):  
    return database.search_keyword(keyword)
    