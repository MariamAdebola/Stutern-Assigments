import sqlite3
from database_connect import conn
from database_connect import cursor

cursor.execute("""
                 CREATE TABLE celebrity (
                     name TEXT,
                     genre TEXT,
                     num_albums INTEGER,
                     age INTEGER,
                     awards INTEGER,
                     years_in_industry INTEGER
                 )
 """)

print("table created successfully")
