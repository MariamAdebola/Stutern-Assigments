import sqlite3
from unicodedata import name
from database_connect import conn
from database_connect import cursor

celeb_list = [
     ('Omotola Jolade','Drama', 228, 55, 32, 22),
     ('Saint Obi','Comedy', 3, 33, 2, 9),
     ('Chika Ike','Drama', 43, 40, 12, 18),
     ('Lateef Oladimeji','Thriller', 29, 35, 5, 17),
     ('Regina Daniels','Fantasy', 28, 22, 5, 6),
     ('Chidi Mokeme','Action', 77, 62, 16, 35),
     ('Genevieve Nnaji','Drama', 140, 52, 50, 19),
     ('Joke Silva','Thriller', 98, 65, 24, 53),
     ('Funke Akindele','Comedy', 122, 42, 48, 25),
     ('Muyiwa Ademola','Drama', 67, 51, 19, 35),
     ('Yinka Quadri','Horror', 83, 51, 23, 33),
     ('Oge Okoye','Mystery', 25, 42, 12, 24),
     ('Iyabo Ojo','Comedy', 75, 42, 33, 28),
     ('Toyin Abraham','Action', 45, 25, 8, 12),
     ('Jacob Silva','Thriller', 24, 62, 24, 35),
     ('Sukanmi Omobolanle', 'Comedy', 102, 42, 48, 25),
     ('Kunle Johnson','Drama', 88, 42, 12, 18),
     ('Tunde Ednut','Comedy', 25, 42, 12, 24),
     ('Mr Latin','Comedy', 25, 42, 12, 24),
     ('Mary Ade','Drama', 59, 42, 12, 24),
     ('Mercy Johnson','Thriller', 44, 34, 8, 12),
     ('Jide Kosoko','Drama', 60, 19, 8, 12),
     ('Femi Adebayo','Drama', 37, 22, 8, 12),
     ('Osas Ighodaro','Drama', 34, 25, 8, 12)
]

#insert values into celebrity table
cursor.executemany('INSERT INTO celebrity VALUES(?, ?, ?, ?, ?, ?)', celeb_list)


#1. get the most decorated celebrity

def most_decorated_celeb(column_1="name", column_2="awards"):

    query = f"""
    SELECT {column_1}, {column_2}
    FROM celebrity 
    ORDER BY {column_2} DESC
    LIMIT 1
    """

    cursor.execute(query)

    items = cursor.fetchall()

    print(f'{column_1}' + '\t\t' + f'{column_2}')

    print(f"{'-' * 22}")

    for item in items:
        column_1, column_2 = item
        print(f"{column_1:21}{column_2}")

#call the function
most_decorated_celeb("name", "awards")

#2. get the oldest celebrity

def oldest_celeb(column_1="name", column_2="age"):

    query = f"""
    SELECT {column_1}, {column_2}
    FROM celebrity 
    ORDER BY {column_2} DESC
    LIMIT 1
    """

    cursor.execute(query)

    items = cursor.fetchall()

    print(f'{column_1}' + '\t\t ' + f'{column_2}')

    print(f"{'-' * 22}")

    for item in items:
        column_1, column_2 = item
        print(f"{column_1:21}{column_2}")

#call the function
oldest_celeb("name", "age")

#3. get the celeb with the longest years in the industry

def with_longest_years(column_1="name", column_2="years_in_industry"):

    query = f"""
    SELECT {column_1}, {column_2}
    FROM celebrity 
    ORDER BY {column_2} DESC
    LIMIT 1
    """

    cursor.execute(query)

    items = cursor.fetchall()

    print(f'{column_1}' + '\t\t' + f'{column_2}')

    print(f"{'-' * 22}")

    for item in items:
        column_1, column_2 = item
        print(f"{column_1:21}{column_2}")

#call the function
with_longest_years("name", "years_in_industry")

#4. get the celebrity with the least number of albums

def least_album(column_1="name", column_2="num_albums"):

    query = f"""
    SELECT {column_1}, {column_2}
    FROM celebrity 
    ORDER BY {column_2}
    LIMIT 1
    """

    cursor.execute(query)

    items = cursor.fetchall()

    print(f'{column_1}' + '\t\t' + f'{column_2}')

    print(f"{'-' * 22}")

    for item in items:
        column_1, column_2 = item
        print(f"{column_1:21}{column_2}")

#call the function
least_album("name", "num_albums")

#5. get the most popular genre

def popular_genre(column="genre"):

    query = f"""
    SELECT COUNT(DISTINCT {column})
    FROM celebrity 
    ORDER BY COUNT(DISTINCT {column}) DESC
    """

    cursor.execute(query)

    items = cursor.fetchall()

    print(f'{column}')

    print(f"{'-' * 15}")

    for item in items:
        print(f"{item}")

#call the function
popular_genre("genre")

#commit to database
conn.commit()

#close connection
conn.close()
