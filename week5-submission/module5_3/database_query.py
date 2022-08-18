import sqlite3
import csv

#connect to a database
conn = sqlite3.connect("inventory.db")

#create a cursor
cursor = conn.cursor()


# 1. the amount the business owner invested in the procurement of the items.

cursor.execute("""SELECT SUM(cost_price) FROM stationery_table; """)

query1= cursor.fetchall()

for row in query1:
    print(f"The total amount invested is {row[0]}")


2. # Calculate the average quantity of items in stock

cursor.execute("""SELECT Round(AVG(Quantity)) FROM stationery_table; """)

query2= cursor.fetchall()

for row in query2:
    print(f"The average quantity of items is {row[0]}")


3. # item with the least quantity in stock

cursor.execute("""SELECT MIN(Quantity) FROM stationery_table; """)

query3= cursor.fetchall()

for row in query3:
    print(f"The least quantity of items is {row[0]}")


4. # Determine the item with the most quantity in stock

cursor.execute("""SELECT MAX(Quantity) FROM stationery_table; """)

query4= cursor.fetchall()

for row in query4:
    print(f"The maximum quantity of items is {row[0]}")


conn.commit()

conn.close()
