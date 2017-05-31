import mysql.connector
from mysql.connector import errorcode

try:
    cnn = mysql.connector.connect(
        user='root',
        password='Admin123',
        host='localhost',
        database='test')
    print("Connected!")
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User or Password invalid!")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist!")
    else:
        print(e)

cursor = cnn.cursor()

addName =("INSERT INTO name (firstName, lastName) VALUES (%s, %s)")
firstName = "John"
lastName = "DOE"
fullName=(firstName, lastName)

cursor.execute(addName,fullName)

cnn.commit()
cursor.close()
cnn.close()