from PyQt5.QtWidgets import QTableWidgetItem
import sqlite3

class BaseDeDatos:

    def __init__(self):
        self.conexion = sqlite3.connect("MODELO/db.db")
        self.cursor = self.conexion.cursor()

    def getDatos(self):
        self.cursor.execute("SELECT * FROM personas")
        datos = self.cursor.fetchall()
        return datos
