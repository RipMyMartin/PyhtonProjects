from sqlite3 import connect, Error
from os import path

def create_connect(path:str):
    connection = None
    try:
        connection = connect(path)
        print("Connection established or data inserted")
    except Error as e:
        print(f"Error occurred: {e}")
    return connection

def execute_query(connection, query, data=None):
    try:
        cursor = connection.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        connection.commit()
        print("Query executed successfully!")
    except Error as e:
        print(f"Error occurred: {e}")

def execute_read_query(connection, query, data=None):
    cursor = connection.cursor()
    result = None
    try:
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error occurred: {e}")
    finally:
        cursor.close()

def dropTable(connection,table):
    try:
        cursor = connection.cursor()
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
        connection.commit()
        #print ("Tabel on kustatud.")
    except Error as e:
        print (f"Tekkis viga:{e}")

def select_users_by_name(connection, name):
    query = "SELECT * FROM users WHERE Name = ?"
    data = (name,)
    users = execute_read_query(connection, query, data)
    return users

create_users_table = """
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
firstName TEXT NOT NULL,
lastName TEXT NOT NULL,
age INTEGER,
birthday DATETIME,
gender TEXT,
pets TEXT NOT NULL
);
"""

insert_users = """
INSERT INTO
users (firstName, lastName, age, birthday, gender, pets)
VALUES
('Martin', 'Sild', 16, '2007-09-09', 'Male', 'Dog'),
('Annika', 'Kizilova', 16, '2007-12-20', 'Female', 'Cat'),
('Dmitii', 'Gelivoma', 17, '2007-08-15', 'Female', 'Dog'),
('Jana', 'Zandarova', 17, '2007-03-25', 'Female', 'Parrot');
"""

create_auto_table = """
CREATE TABLE IF NOT EXISTS auto(
id INTEGER PRIMARY KEY AUTOINCREMENT,
Brand TEXT NOT NULL,
Model TEXT NOT NULL,
Year INTEGER,
Owner_ID INTEGER,
FOREIGN KEY (Owner_ID) REFERENCES users (id)
);
"""

insert_auto = """
INSERT INTO
auto (Brand, Model, Year, Owner_ID)
VALUES
('BMW', 'X5', 2017, 3),
('Audi', 'A4', 2016, 4),
('Toyota', 'Corolla', 2018, 1),
('Honda', 'Civic', 2019, 2)
"""

select_auto = "SELECT * FROM auto"
select_users = "SELECT * FROM users"

filename = path.abspath(__file__)
dbdir = path.dirname(filename)
dbpath = path.join(dbdir, "data.db")
conn = create_connect(dbpath)

execute_query(conn, create_users_table)
execute_query(conn, insert_users)
users = execute_read_query(conn, select_users)
print("Users table:")
for user in users:
    print(user)

execute_query(conn, create_auto_table)
execute_query(conn, insert_auto)
autos = execute_read_query(conn, select_auto)
print("Autos:")
for auto in autos:
    print(auto)

insert_user = (
    input("Eesnimi: "),
    input("Perenimi: "),
    int(input("Vanus: ")),
    input("Sünnikuupäev (YYYY-MM-DD): "),
    input("Sugu: "),
    input("Lemmikloom: ")
)
execute_query(conn, "INSERT INTO users(firstName,lastName, age, birthday, gender, pets) VALUES (?, ?, ?, ?, ?, ?)", insert_user)

def select_users_by_same_pet(connection, pet):
    query = """
    SELECT u.*
    FROM users u
    WHERE u.pets = ?
    """
    data = (pet,)
    users = execute_read_query(connection, query, data)
    return users

# Пользователь вводит своего любимого питомца
favorite_pet = input("Введите своего любимого питомца: ")

# Ищем пользователей с таким же любимым питомцем
users_with_same_pet = select_users_by_same_pet(conn, favorite_pet)

# Выводим результат
if users_with_same_pet:
    print(f"Люди, у которых есть {favorite_pet}:")
    for user in users_with_same_pet:
        print(user)
else:
    print(f"Никто из пользователей не имеет питомца с именем {favorite_pet}.")



