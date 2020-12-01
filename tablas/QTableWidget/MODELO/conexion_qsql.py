from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QTableWidgetItem

class BaseDeDatos:

    def __init__(self):
        self.bd = QSqlDatabase.addDatabase("QSQLITE")
        self.bd.setDatabaseName("MODELO/db.db")
        self.bd.open()
        print("Conexión exitosa:", self.bd.open())

    def cargarTabla(self, tabla):
        self.query = QSqlQuery()
        self.query.prepare("SELECT * FROM personas")
        self.query.exec_()
        columnas = self.query.record().count()
        fila = 0
        tabla.setColumnCount(columnas)
        while self.query.next():
            tabla.insertRow(fila)
            for columna in range(columnas):
                tabla.setItem(fila, columna, QTableWidgetItem(str(self.query.value(columna))))
            fila += 1
