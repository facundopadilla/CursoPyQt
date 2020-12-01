from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from VISTA.ui_qtableview import Ui_Form
import sys

class TablaView(QDialog):

    def __init__(self):
        super(TablaView, self).__init__()
        self.tabla = Ui_Form()
        self.tabla.setupUi(self)

        # Crear modelo

        filas = 2
        columnas = 3
        model = QStandardItemModel(filas, columnas)
        header = ["Columna 1", "Columna 2", "Columna 3"]
        datos = [["Dato 1", "Dato 2", "Dato 3"], ["Dato 4", "Dato 5", "Dato 6"]]

        model.setHorizontalHeaderLabels(header)
        for fila in range(len(datos)):
            for columna in range(len(header)):
                model.setItem(fila, columna, QStandardItem(datos[fila][columna]))

        self.tabla.tableView.setModel(model)

        self.tabla.tableView.doubleClicked.connect(self.prueba)

        self.tabla.tableView.setRowHidden(1, True)

        print(self.tabla.tableView.model().index)

    def prueba(self, dato):
        print(dato.row(), dato.column())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_aplicacion = TablaView()
    mi_aplicacion.show()
    sys.exit(app.exec_())
