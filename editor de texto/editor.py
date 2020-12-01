from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCloseEvent
from VISTA.ui_editor import Ui_Editor
import sys, eventos

class Editor(QMainWindow):

    def __init__(self):
        super(Editor, self).__init__()
        self.editor = Ui_Editor()
        self.editor.setupUi(self)
        self.control = 0
        self.titulo = "Editor de texto"

        # --- Text changed ---
        self.editor.textEdit.textChanged.connect(self.textChanged)
        # --- Abrir archivo ---
        self.editor.actionAbrir.triggered.connect(lambda: self.abrirArchivo())
        self.editor.actionNuevo.triggered.connect(lambda: self.nuevoArchivo())
        self.editor.actionGuardar_como.triggered.connect(lambda: self.guardarComo())

    def nuevoArchivo(self):
        self.control = self.validar(2)
        if self.control:
            self.editor.textEdit.setText("")
            self.setWindowTitle("Editor de texto")

    def abrirArchivo(self):
        self.control = self.validar(1)
        if self.control:
            self.titulo = eventos.abrirArchivo(
            QFileDialog(),
            self.editor.textEdit,
            self,
            )

    def guardarComo(self):
        eventos.guardarComo(
            QFileDialog(),
            self.editor.textEdit,
            self,
        )

    def textChanged(self):
        if self.titulo == "Editor de texto" or self.titulo == "Editor de texto - *":
            self.titulo = "Editor de texto - *"
        else:
            self.titulo = f"Editor de texto - {self.titulo} *"
        self.setWindowTitle(self.titulo)
        self.control = 1

    def validar(self, tipo):
        if "*" in str(self.titulo):
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Alerta")
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            btnSi = msgbox.button(QMessageBox.Yes).setText("Si")
            if tipo == 1:
                msgbox.setText("Estás a punto de abrir un nuevo archivo sin guardar cambios, ¿desea continuar?")
            elif tipo == 2:
                msgbox.setText("Estás a punto de crear un nuevo texto sin guardar cambios, ¿deseas continuar?")
            elif tipo == 3:
                msgbox.setText("Estás a punto de cerrar el programa sin guardar cambios, ¿deseas continuar?")
            respuesta = msgbox.exec_()
            if respuesta == QMessageBox.Yes:
                return 1
            elif respuesta == QMessageBox.No:
                return 0

    def closeEvent(self, event: QCloseEvent):
        self.control = self.validar(3)
        if self.control:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_aplicacion = Editor()
    mi_aplicacion.show()
    sys.exit(app.exec_())
