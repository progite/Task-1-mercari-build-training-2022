import sqlite3
import random
conn = sqlite3.connect("mercari.sqlite3", check_same_thread=False)
cursor = conn.cursor()
try:
    cursor.execute(
        "create table category(id TEXT PRIMARY KEY, name TEXT NOT NULL);")
except:
    # print("Cannot create database ")
    pass


def get_category_id(category_name):
    cursor.execute("select id from category where name=?", (category_name,))
    if len(cursor.fetchall()) == 0:
        print("Generating new category id")
        category_id = str(random.randint(0, 10**6))
        cursor.execute(
            "insert into category(id, name) VALUES (?,?); ", (category_id, category_name))
    cursor.execute("select id from category where name=?", (category_name,))
    row = cursor.fetchall()[0]
    cursor.close()
    return row  # returns category id


def get_category_name(category_id):
    cursor.execute("select name from category where id=?", (category_id[0],))
    return cursor.fetchall()[0]

# category_id = get_category_id("random")
# print(category_id, get_category_name(category_id))
# cursor.close()