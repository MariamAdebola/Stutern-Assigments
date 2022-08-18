import sqlite3
from database_connect import conn
from database_connect import cursor


#create the table for the stationery
cursor.execute("""
    CREATE TABLE stationery_table (ID INTEGER,
                                Name TEXT,
                                cost_price INTEGER,
                                Quantity INTEGER) """)

print("table created successfully")
