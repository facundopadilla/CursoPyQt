from PyQt5.QtGui import QStandardItem
from PyQt5.QtWidgets import QTableWidgetItem

def enviar_a_view(fila, tableWidget, tableView):
    items = [tableWidget.item(fila, 0).text(),
             tableWidget.item(fila, 1).text(),
             tableWidget.item(fila, 2).text(),
             tableWidget.item(fila, 3).text(),
             tableWidget.item(fila, 4).text()]
    fila = tableView.model().rowCount()
    columna = 0
    for item in items:
        tableView.model().setItem(fila, columna, QStandardItem(item))
        columna += 1
    tableView.model().layoutChanged.emit()

def enviar_a_widget(fila, tableWidget, tableView):
    items = [tableView.model().index(fila, columna).data() for columna in range(5)]
    fila = tableWidget.rowCount()
    columna = 0
    tableWidget.insertRow(fila)
    for item in items:
        tableWidget.setItem(fila, columna, QTableWidgetItem(item))
        columna += 1
