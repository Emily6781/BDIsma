import mysql.connector

def conexion():
    connection = mysql.connector.connect(
        host= "localhost",
        user = "root",
        password = "",
        database = "practica"
    )
    return connection
