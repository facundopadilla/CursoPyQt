from PySide2.QtWidgets import *
from .UI.ui_ventanaAdd import Ui_VentanaAdd
import sys

class VentanaAdd(QDialog):

    def __init__(self):
        super(VentanaAdd, self).__init__()
        self.widgets = Ui_VentanaAdd()
        self.widgets.setupUi(self)

        self.widgets.btnAdd.clicked.connect(lambda: self.getDatos())

    def mostrar(self):
        self.show()

    def getDatos(self):
        datos = [
            self.widgets.lineNombre.text(),
            self.widgets.lineApellido.text(),
            self.widgets.lineDni.text(),
            self.widgets.lineDireccion.text(),
            self.widgets.lineTel.text(),
            self.widgets.lineFoto.text(),
        ]
        return datos

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_aplicacion = Tabla()
    mi_aplicacion.show()
    sys.exit(app.exec_())
