from PyQt5.QtWidgets import *
from VISTA.ui_formulario import Ui_MainWindow
import sys, eventos

class Registro(QMainWindow):

    def __init__(self):
        super(Registro, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resultado = 0

        # --- Eventos ---
        self.ui.lineNombre.textChanged.connect(lambda: eventos.validarTexto(self.ui.lineNombre))
        self.ui.lineApellido.textChanged.connect(lambda: eventos.validarTexto(self.ui.lineApellido))
        self.ui.lineDireccion.textChanged.connect(lambda: eventos.validarDireccion(self.ui.lineDireccion))
        self.ui.lineTel.textChanged.connect(lambda: eventos.validarNumero(self.ui.lineTel))
        self.ui.spinEdad.valueChanged.connect(lambda: eventos.validarEdad(self.ui.spinEdad))

        # --- Botón: registro ---
        self.ui.btnRegistrarse.clicked.connect(lambda: eventos.validarRegistro([
            self.ui.lineNombre,
            self.ui.lineApellido,
            self.ui.lineDireccion,
            self.ui.lineTel,
            self.ui.spinEdad,
            self
        ]))
        self.ui.btnRegistrarse.clicked.connect(self.alerta)

    def alerta(self):
        msgbox = QMessageBox()
        msgbox.setWindowTitle("Alerta")
        if self.resultado == 1:
            msgbox.setText("¡Registrado con éxito!")
        elif self.resultado == 2:
            msgbox.setText("¡Verificá los campos!")
        msgbox.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_aplicacion = Registro()
    mi_aplicacion.show()
    sys.exit(app.exec_())
