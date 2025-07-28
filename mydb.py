import mysql.connector
dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="pass123",
)
#preparing a cursor object
cursorObject = dataBase.cursor()

#creating a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS djangocrm_db")  
print("Database created successfully!")