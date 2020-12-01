from PySide2.QtWidgets import *
from VISTA.UI.ui_tabla import Ui_Tabla
from VISTA.ventanaAdd import VentanaAdd
import sys

class Tabla(QMainWindow):

    def __init__(self):
        super(Tabla, self).__init__()
        self.tabla = Ui_Tabla()
        self.tabla.setupUi(self)
        self.ventanaAdd = VentanaAdd()
        self.datos = None

        # --- Tabla --
        self.tabla.btnAdd.clicked.connect(lambda: self.abrirVentana("add"))
        # --- Ventana Add ---
        self.ventanaAdd.widgets.btnAdd.clicked.connect(lambda: self.mostrarDatos("add"))
        # --- Ventana

    def abrirVentana(self, tipo):
        if tipo == "add":
            self.ventanaAdd.mostrar()
        elif tipo == "borrar":
            pass

    def mostrarDatos(self, tipo):
        if tipo == "add":
            datos = self.ventanaAdd.getDatos()
            print(datos)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_aplicacion = Tabla()
    mi_aplicacion.show()
    sys.exit(app.exec_())
