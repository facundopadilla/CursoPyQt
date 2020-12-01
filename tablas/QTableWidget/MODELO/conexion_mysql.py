import pymysql

# puede ser mysql.connector o pymysql, ustedes utilizan el que más les guste

class BaseDeDatos:

    def __init__(self):
        self.conexion = pymysql.connect(
            host="dirección del host",
            user="tu usuario",
            password="tu contraseña",
            database="nombre de la base de datos",
        )
        self.cursor = self.conexion.cursor()

    def getDatos(self):
        self.cursor.execute("SELECT * FROM actor")
        datos = self.cursor.fetchall()
        return datos
