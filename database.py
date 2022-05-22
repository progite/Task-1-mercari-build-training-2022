from msilib.schema import Error
import sqlite3


conn = sqlite3.connect("mercari.sqlite3", check_same_thread= False)
cursor = conn.cursor()
try:
    cursor.execute(
        "create table items(id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL);")
except:
    pass


def insert_values(id, name, category):
    try:
        cursor.execute(
            "insert into items(id, name, category) VALUES (?,?, ?);", (id, name, category))

    except:
        print("ERROR!!")
        pass


def search_keyword(name: str):
    print("Entered Here")
    cursor.execute("select category from items where name=?", (name,))
    dict_items = {"items": []}
    for row in cursor.fetchall():
        dict_items["items"].append({"name": name, "category": row[0]})
    return dict_items


def display_db():
    cursor.execute("SELECT * FROM items")
    for row in cursor.fetchall():
        print(row)


# insert_values(3,"test","trial")
# search_keyword("test")
# display_db()
