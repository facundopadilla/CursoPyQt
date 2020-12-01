from .conexion import BaseDeDatos
from PyQt5.QtWidgets import QTableWidgetItem

def cargarTabla(tabla):
    bd = BaseDeDatos()
    datos = bd.getDatos()
    tabla.setRowCount(len(datos))
    tabla.setColumnCount(len(datos[0]))
    for fila in range(len(datos)):
        for columna in range(len(datos[fila])):
            tabla.setItem(fila, columna, QTableWidgetItem(str(datos[fila][columna])))
