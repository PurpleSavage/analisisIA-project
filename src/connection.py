import mysql.connector
from mysql.connector import Error


class ConnectionDb:
    def __init__(self):
       self.host='localhost'
       self.database='reconocimiento_facial'
       self.user='root'
       self.password='jeanpaul'
    
    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Conexión establecida con la base de datos")
                return self.connection
        except Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexión cerrada")
