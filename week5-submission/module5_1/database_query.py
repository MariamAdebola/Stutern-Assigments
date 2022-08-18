import sqlite3
from database_connect import conn
from database_connect import cursor

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

#get the items to restock

query = (f"""
        SELECT DISTINCT Name, cost_price, Quantity,
        CASE
        WHEN Quantity > 15 THEN "Sufficient"
        ELSE "Restock"
        END AS "Stock_option"
        FROM stationery_table
        ORDER BY cost_price DESC;
    """)
    
cursor.execute(query)

items = cursor.fetchall()

print(f'{"Name"}' + '\t\t' + f'{"cost_price"}' + '\t' + f'{"Quantity"}' + '\t' + f'{"Stock_option"}')

print(f"{'-' * 65}")

for item in items:
    Name, cost_price, Quantity, Stock_option = item
    print(f"{Name:11}{cost_price:10}{Quantity:19}\t{Stock_option}")

#commit to database
conn.commit()

#close connection
conn.close()
