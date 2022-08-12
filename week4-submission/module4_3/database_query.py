import sqlite3
from database_connect import conn
from database_connect import cursor

student_list = [
     ('Eniola','Osadare','eniosadare@gmail.com','Data Science'),
     ('Lawrence','Aneshi','lawaneshi@gmail.com','Data Science'),
     ('Eke','Ihuoma','ekeihuoma@gmail.com','Data Science'),
     ('Angela','Emmanuel','angelaemmanuel@gmail.com','Data Science'),
     ('Seyi','Nichiolas','seyinichiolas@gmail.com','Data Science'),
     ('Doyinsola','Esan','doyinsolaesan@gmail.com','Data Science'),
     ('Kenny','Ayan','kennyayan@gmail.com','Data Science'),
     ('Doyinsola','Esan','doyinsolaesan@gmail.com','Data Science'),
     ('Aishat','Abass','aishatabass@gmail.com','Data Science'),
     ('Jide','Adesugba','jideadesugba@gmail.com','Data Science'), 
     ('Faith','Amure','faithamure@gmail.com','Data Science'),
     ('Deborah','Olorunnishola','debbyolorunnishola@gmail.com','Data Science'),
     ('Kafayat','Ibrahim','kafayatibrahim@gmail.com','Data Science'),
     ('Cynthia','Awiya','cynthiaawiya@gmail.com','Data Science'),
     ('Stephen','Ogungbile','stephenogunbile@gmail.com','Data Science'),
     ('Christian','Uzondu','christianuzondu@gmail.com','Data Science'),
     ('Theresa','Karamor','theresakaramor@gmail.com','Data Science'),
     ('Uyateide','Tina','uyateidetina@gmail.com','Data Science'),
     ('Bukola','Ajayi','bukolaajayi@gmail.com','Data Science'),
     ('Gideon','George','sgideongeorge@gmail.com','Data Science'),
     ('Abubakar','Adisa','abubakaradisa@gmail.com','Data Science'),
     ('Deborah','Adesanya','deborahadesanya@gmail.com','Data Science'),
     ('Ogechi','Njemanze','ogechinjemanze@gmail.com','Data Science'),
     ('Vic','Chukwuno','vicchukwuno@gmail.com','Data Science'),
     ('Ganiyat','Shittu','ganiyatshittu@gmail.com','Data Science'),
     ('Omowunmi', 'Awoniran','omowunmiawoniran@gmail.com','Data Science'),
     ('Tawakalitu','Awonaike','tawakalituawonaike@gmail.com','Data Science'),
     ('Afolabi', 'Ade','afolabiade@gmail.com','Data Science'),
     ('Ramotallah','Jubril','ramotallahjubril@gmail.com','Data Science'),
     ('Joyce','Ezeonwu','joyceezeonwu@gmail.com','Data Science'),
     ('Mariam','Adeoti','mariamadeoti@gmail.com','Data Science'),
     ('Praise','Emmanuel','praiseemmanuel@gmail.com','Data Science'),
     ('Kehinde','Orolade','kehindeorolade@gmail.com','Data Science'),
     ('Temitope','Bamidele','temitopbamidele@gmail.com','Data Science'),

]

# cursor.executemany('INSERT INTO SGA_students VALUES(?, ?, ?, ?)', student_list)

# #check the new values
# cursor.execute('SELECT * FROM SGA_students')

# items = cursor.fetchall()

# #format the headers of the table
# print('first_name' + '\tlast_name' + '\t\temail' + "\t\t\tcourse_type")
# print ('--------' + '\t-------' + '\t\t-------------------' + '\t\t------')

# for item in items:
#      first_name, last_name, email, course_type = item
#      print(f"{first_name:15}{last_name:15}{email:22}\t\t{course_type}") 

# #change the table name
# cursor.execute('ALTER TABLE SGA_students RENAME TO SGA_student')
# print("table name updated successfully")

# #add a new column to the table
# cursor.execute('ALTER TABLE SGA_student ADD graduation_month text')
# print("new column added successfully")


#Add values to the new column
graduation = ['February 2022']


cursor.execute("UPDATE SGA_student SET graduation_month = 'graduation'")
print("values updated to the graduation_month column")

# check the new values
cursor.execute('SELECT * FROM SGA_student')

items = cursor.fetchall()

#format the headers of the table
print('first_name' + '\tlast_name' + '\t\temail' + "\t\t\tcourse_type" + '\t\tgraduation_month')
print ('--------' + '\t-------' + '\t\t-------------------' + '\t\t------' + '\t\t------')

for item in items:
     first_name, last_name, email, course_type, graduation_month = item
     print(f"{first_name:15}{last_name:15}{email:22}\t\t{course_type}{graduation_month}") 



# # commit to database
# conn.commit()

# #close connection
# conn.close()