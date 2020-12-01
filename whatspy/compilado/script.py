from PySide2.QtWidgets import QDialog, QApplication, QSizeGrip
from PySide2.QtCore import Qt
from VISTA.ui_whatspy import Ui_Whatspy

import sys, eventos


class WhatsPy(QDialog):

    def __init__(self):
        super(WhatsPy, self).__init__()
        self.programa = Ui_Whatspy()
        self.programa.setupUi(self)
        self.programa.grip = QSizeGrip(self.programa.lblGrip)
        self.controlVentana = 0
        self.programa.btnExportar.setEnabled(False)

        # Datos

        self.fila_numeros = None
        self.fila_valores = None

        # Mover ventana - Global

        def moverVentana(event):
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.programa.Contenedor.mouseMoveEvent = moverVentana

        # Botones
        self.programa.btnVerde.clicked.connect(lambda: eventos.minimizarVentana(self))
        self.programa.btnAmarillo.clicked.connect(lambda: self.estadoVentana())
        self.programa.btnRojo.clicked.connect(lambda: eventos.cerrarVentana(self))

        # Botones funcionales
        self.programa.btnAbrir.clicked.connect(lambda: self.getChat())
        self.programa.btnExportar.clicked.connect(lambda: eventos.exportarChat(self.fila_numeros, self.fila_valores))

    def getChat(self):
        try:
            datos = eventos.abrirChat(self.programa.tableWidget, self.programa.btnExportar, self.programa.label)
            self.fila_numeros = datos[0]
            self.fila_valores = datos[1]
        except:
            pass
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


    def estadoVentana(self):
        if self.controlVentana:
            eventos.normalizarVentana(self)
            self.controlVentana = 0
        else:
            eventos.maximizarVentana(self)
            self.controlVentana = 1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_programa = WhatsPy()
    mi_programa.show()
    sys.exit(app.exec_())
