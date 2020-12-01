from PySide2.QtWidgets import *
from .UI.ui_ventana2 import Ui_Ventana2
import sys

class Ventana2(QDialog):

    def __init__(self):
        super(Ventana2, self).__init__()
        self.widgets = Ui_Ventana2()
        self.widgets.setupUi(self)

    def mostrar(self):
        self.show()

    def setInformacion(self, datos):
        self.widgets.lineDos.insert(datos)

    def getDatos(self):
        datos = self.widgets.lineDos.text()
        return datos

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana2 = Ventana2()
    ventana2.show()
    sys.exit(app.exec_())
