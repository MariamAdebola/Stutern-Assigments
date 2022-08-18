import sqlite3
import csv

#connect to a database
conn = sqlite3.connect("inventory.db")

#create a cursor
cursor = conn.cursor()

#create the table for the stationery

cursor.execute("""
    CREATE TABLE stationery_table (ID INTEGER,
                                Name TEXT,
                                cost_price INTEGER,
                                Quantity INTEGER) """)

print("table created successfully")


#create a list of items for the table

item_list = [
            (1, 'Pen', 150, 35), 
            (2, 'Eraser', 50, 18), 
            (3, 'Sharpener', 100, 25), 
            (4, 'Push Pin', 1000, 33),
            (5, 'Marker', 1500, 10), 
            (6, 'Pencil', 50, 4), 
            (7, 'Book', 450, 74),
            (8, 'Notepad', 6500, 5), 
            (9, 'Journal', 7000, 7),
            (10, 'Envelope', 250, 15), 
            (11, 'Ruler', 50, 15)
            ]

#insert values into the table
cursor.executemany('INSERT INTO stationery_table VALUES(?, ?, ?, ?)', item_list)
print("successful")

conn.commit()

conn.close()
