from datetime import datetime

import mysql.connector

db = mysql.connector.connect(user='root', password='password',
                              host='localhost', database = "test1")

mycursor = db.cursor()

# mycursor.execute("CREATE TABLE person (name VARCHAR(50), age INT UNSIGNED, personID INT PRIMARY KEY AUTO_INCREMENT )")

# mycursor.execute("DESCRIBE person")
#
# for x in mycursor:
#     print(x)
#
# age = 26
# name = "eren"
# mycursor.execute(f"INSERT INTO person (age, name) VALUES ({age}, {name})")
# mycursor.execute("INSERT INTO person (age, name) VALUES (%s, %s)", (age, name))
# db.commit()
# mycursor.execute()

# mycursor.execute("SELECT * FROM person")
# for x in mycursor:
#     print(x)

# mycursor.execute("CREATE TABLE table2 (name varchar(50), created datetime, gender ENUM(\"M\",\"F\"), id INT PRIMARY KEY AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO table2 (name, created, gender) VALUES (%s, %s, %s)", ("eren", datetime.now(), "M"))
# mycursor.execute("INSERT INTO table2 (name, created, gender) VALUES (%s, %s, %s)", ("Fus", datetime.now(), "F"))
# mycursor.execute("INSERT INTO table2 (name, created, gender) VALUES (%s, %s, %s)", ("Orhan", datetime.now(), "M"))
# db.commit()

mycursor.execute("SELECT id, name FROM table2 WHERE gender = \"M\" ORDER BY id DESC")
for x in mycursor:
    print(x)


