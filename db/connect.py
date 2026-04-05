import mysql.connector
def conectar():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Moniq3421@",
        database="sistema"
    )

    return conn
