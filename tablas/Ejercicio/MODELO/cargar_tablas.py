from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from .conexion import BaseDeDatos

bd = BaseDeDatos()

def cargarTableWidget(tabla):
    global bd
    datos = bd.getDatos()
    tabla.setRowCount(len(datos))
    tabla.setColumnCount(len(datos[0]))
    for fila in range(len(datos)):
        for columna in range(len(datos[fila])):
            tabla.setItem(fila, columna, QTableWidgetItem(str(datos[fila][columna])))

def cargarTableView(tabla):
    global bd
    datos = bd.getDatos()
    filas = len(datos)
    columnas = len(datos[0])
    model = QStandardItemModel(filas, columnas)
    for fila in range(filas):
        for columna in range(columnas):
            model.setItem(fila, columna, QStandardItem(str(datos[fila][columna])))
    tabla.setModel(model)
