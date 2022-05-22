from msilib.schema import Error
import sqlite3

from category_database import get_category_id, get_category_name


conn = sqlite3.connect("mercari.sqlite3", check_same_thread=False)
cursor = conn.cursor()

def generate_table():
    try:
        cursor.execute(
            "create table items(id INTEGER PRIMARY KEY, name TEXT NOT NULL, category_id TEXT NOT NULL, image_filename TEXT NOT NULL);")
    except:
        pass


def insert_values(id, name, category, image_filename):
    try:
        category_id = get_category_id(category)
        # print("Category id", category_id[0])
        # print("insert into items(id, name, category_id, image_filename) VALUES (?,?, ?, ?);", (id, name, category_id[0], image_filename))
        cursor.execute(
            "insert into items(id, name, category_id, image_filename) VALUES (?,?, ?, ?);", (id, name, category_id[0], image_filename))
        # print("successfully inserted values")
    except:
        print("ERROR!!")
        pass


def search_keyword(name: str):
    cursor.execute("select category from items where name=?", (name,))
    dict_items = {"items": []}
    for row in cursor.fetchall():
        dict_items["items"].append({"name": name, "category": row[0]})
    return dict_items


def get_item_by_id(item_id: int):
    cursor.execute("select name,category_id,image_filename from items where id=?",(item_id,))
    row = cursor.fetchall()
    print("in get_item_by_id ", row)
    category = get_category_name(row[1]) #gets category name from table category
    for row in cursor.fetchall():
        return {"name": row[0], "category": category, "image:": row[2]}


def display_db():
    cursor.execute("SELECT * FROM items")
    for row in cursor.fetchall():
        print(row)

# generate_table()
# insert_values(4,"test","trial","ccf089e0647c85216169cdfca5848c15e21f1fc93c1143b644a6b8a22dc7080e.jpg")
# get_item_by_id(3)
# print("found",get_item_by_id(3))
# search_keyword("test")
# display_db()
# cursor.close()