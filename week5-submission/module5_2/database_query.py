import sqlite3
import csv

#connect to a database
conn = sqlite3.connect("StudentResults.db")

#create a cursor
cursor = conn.cursor()

#1. student with the highest score in Maths

cursor.execute("""SELECT Name, MAX(Math) FROM students; """)

query1 = cursor.fetchall()

for row in query1:
    print(f"The best performing student in Math is {row[0]} with {row[1]} points")

# 2. Student with the lowest score in english

cursor.execute("""SELECT Name, MIN(English) FROM students; """)

query2 = cursor.fetchall()

for row in query2:
    print(f"The best performing student in English is {row[0]} with {row[1]} points")

# 3. Average score of students in Maths

cursor.execute("""SELECT AVG(Math) FROM students; """)

query3= cursor.fetchall()

for row in query3:
    print(f"The average score of student in Math is {row[0]}")

# 4. Average score of students in English

cursor.execute("""SELECT AVG(English) FROM students; """)

query4= cursor.fetchall()

for row in query4:
    print(f"The average score of student in English is {row[0]}")


# 5. the best performing student across all nine subjects in terms of overall scores

cursor.execute("""SELECT Name, (English + Math + Commerce + Biology
              + Physics + French + Yoruba + Economics + Accounting) as
              "Total" FROM students
              Group by Name
              ORDER BY Total DESC
              LIMIT 1; """)

query5= cursor.fetchall()

for row in query5:
    print(f"The best performing student is {row[0]} with {row[1]} points")


# 6. the best performing student across all nine subjects in term of average scores

cursor.execute("""SELECT Name, ROUND((English + Math + Commerce + Biology + Physics + French + Yoruba +
              Economics + Accounting)/9.0) as "Average_Score" FROM students
              Group by Name
              ORDER BY Average_Score DESC
              LIMIT 1; """)

query6= cursor.fetchall()

for row in query6:
    print(f"The student with the higest average score is {row[0]} with {row[1]} points")

conn.commit()

conn.close()
