import sqlite3

#connect to a database
conn = sqlite3.connect("SGA_1_3_learners")

#create a cursor
cursor = conn.cursor()

#check if database has been created
print("database created")
