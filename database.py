from msilib.schema import Error
import sqlite3, random
from unicodedata import category


conn = sqlite3.connect("mercari.sqlite3", check_same_thread=False)
cursor = conn.cursor()

def generate_table():
    try:
        cursor.execute(
            "create table items(id INTEGER PRIMARY KEY, name TEXT NOT NULL, category_id TEXT NOT NULL, image_filename TEXT NOT NULL);")
    except:
        pass

def generate_category():
    try:
        cursor.execute(
            "create table category(id TEXT PRIMARY KEY, name TEXT NOT NULL);")
    except:
        print("Cannot create database category ")
        pass

def insert_values(id, name, category, image_filename):
    cursor.execute("select id from category where name=?", (name,))
    category_id = str(random.randint(0, 10**6)) if len(cursor.fetchall()) == 0 else cursor.fetchall()[0]
    cursor.execute(
        "insert into items(id, name, category_id, image_filename) VALUES (?,?, ?, ?);", (id, name, category_id[0], image_filename))
    try:
        cursor.execute(
            "insert into category(id, name) VALUES (?,?); ", (category_id[0], category))
    except : 
        print("ERROR! Cannot insert category id into category database")
        pass 
        
def get_category_name_from_id(category_id : str):
    cursor.execute("select name from category where id=?",(category_id,))
    return cursor.fetchall()[0]

def search_keyword(name: str):
    # print(name)
    cursor.execute("select category_id from items where name=?", (name,)) #gets all category ids where name = name given 
    rows = cursor.fetchall()
    dict_items = {"items": []}
    for row in rows: #from all category_ids, find category names 
        category_name = get_category_name_from_id(row[0])
        dict_items["items"].append({"name": name, "category": category_name[0]})
    return dict_items


def get_item_by_id(item_id: int):
    cursor.execute("select name,category_id,image_filename from items where id=?",(item_id,))
    row = cursor.fetchall()[0]
    category = get_category_name_from_id(row[1]) #gets category name from table category
    return {"name": row[0], "category": category, "image:": row[2]}

def display_db():
    cursor.execute("SELECT * FROM items")
    for row in cursor.fetchall():
        print(row)

# generate_table()
# insert_values(3,"test","ribulations","debug.jpg")
# insert_values(4,"test","trial","debug.jpg")

# generate_category()
# generate_table()
# get_item_by_id(4)
# print("found",get_item_by_id(3))
# print(search_keyword("test"))
# display_db()
# cursor.close()