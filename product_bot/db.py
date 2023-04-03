import sqlite3


async def db_start():
    global database, cursor
    database = sqlite3.connect("p2.db")
    cursor = database.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS product(
                      id integer primary key, 
                      title varchar ,
                      photo varchar ,
                      description varchar ,
                      price float )""")
    database.commit()


async def all_product():
    products = cursor.execute("""SELECT * FROM product""").fetchall()
    return products


async def add_product(title, photo, description, price):
    product = cursor.execute("""INSERT INTO product (title, photo, description, price) VALUES (?,?,?,?)""",
                             (title, photo, description, price))
    database.commit()
    return product