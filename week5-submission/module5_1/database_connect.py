import sqlite3

#connect to a database
conn = sqlite3.connect("inventory.db")

#create a cursor
cursor = conn.cursor()
