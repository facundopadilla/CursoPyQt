from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from VISTA.ui_qtablewidget import Ui_Form
from MODELO.conexion import BaseDeDatos
from MODELO.cargar_tablas import cargarTabla

import sys

class Tabla(QDialog):

    def __init__(self):
        super(Tabla, self).__init__()
        self.tabla = Ui_Form()
        self.tabla.setupUi(self)

        cargarTabla(self.tabla.tableWidget)



    def mostrarItem(self, fila, columna):
        try:
            print(self.tabla.tableWidget.item(fila, columna).text())
        except:
            pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    tabla = Tabla()
    tabla.show()
    sys.exit(app.exec_())
