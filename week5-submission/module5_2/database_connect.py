import sqlite3
import csv

#connect to a database
conn = sqlite3.connect("StudentResults.db")

#create a cursor
cursor = conn.cursor()

# create the table

cursor.execute("""CREATE TABLE students (
                                Name text,
                                ID integer,
                                English integer,
                                Math integer,
                                Commerce integer,
                                Biology integer,
                                Physics integer,
                                French integer,
                                Yoruba integer,
                                Economics integer,
                                Accounting integer)
            """)
print("table created successfully")

#insert values into the table

with open("2022_waec_result.csv", "r") as open_data:
    
    read_data = csv.reader(open_data)

    next(read_data)

    cursor.executemany('''INSERT INTO students VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
    read_data)
    
    print("success")

conn.commit()

conn.close()
