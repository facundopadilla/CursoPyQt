from PySide2.QtWidgets import *
from VISTA.UI.ui_ventana1 import Ui_Ventana1
from VISTA.subventana import Ventana2
import sys

class Ventana1(QDialog):

    def __init__(self):
        super(Ventana1, self).__init__()
        self.ventana1 = Ui_Ventana1()
        self.ventana1.setupUi(self)
        self.ventana2 = Ventana2()

        self.ventana1.btnAbrir.clicked.connect(lambda: self.ventana2.mostrar())
        self.ventana1.btnUno.clicked.connect(lambda: self.enviarInformacion())

        self.ventana2.widgets.btnDos.clicked.connect(lambda: self.setInformacion())

    def enviarInformacion(self):
        datos = self.ventana1.lineUno.text()
        self.ventana2.setInformacion(datos)

    def setInformacion(self):
        datos = self.ventana2.getDatos()
        self.ventana1.lineUno.insert(datos)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())
