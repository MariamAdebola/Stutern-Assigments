import sqlite3

#connect to a database
conn = sqlite3.connect("celebs")

#create a cursor to execute sql codes
cursor = conn.cursor()

#check if database has been created
print("database created")
