from PyQt5.QtWidgets import *
from PyQt5.QtGui import QCloseEvent, QTextCursor
from VISTA.ui_editor import Ui_Editor
import sys, eventos

class Editor(QMainWindow):

    def __init__(self):
        super(Editor, self).__init__()
        self.editor = Ui_Editor()
        self.editor.setupUi(self)
        self.titulo = "Editor de texto"
        self.ruta = ""
        self.control = 0

    # --- Eventos propios ---
        self.editor.textEdit.textChanged.connect(self.textChanged)
        self.editor.actionNuevo.triggered.connect(lambda: self.nuevoArchivo())
    # --- Eventos externos ---
        self.editor.actionAbrir.triggered.connect(lambda: self.abrirArchivo())
        self.editor.actionGuardar_como.triggered.connect(lambda: self.guardarComo())

    def textChanged(self):
        if self.titulo == "Editor de texto" or self.titulo == "Editor de texto - *":
            self.setWindowTitle("Editor de texto - *")
        else:
            self.setWindowTitle(self.titulo + " *")
        self.control = 1

    def nuevoArchivo(self):
        control = self.validar(1)
        if control:
            self.editor.textEdit.setText("")
            self.setWindowTitle("Editor de texto")
            self.titulo = "Editor de texto"
            self.control = 0

    def abrirArchivo(self):
        control = self.validar(2)
        if control:
            self.ruta = eventos.abrirArchivo(
                QFileDialog(),
                self.editor.textEdit,
                self
            )
            self.titulo = f"Editor de texto - {self.ruta}"
            self.control = 0


    def guardarComo(self):
        aux = self.ruta
        self.ruta = eventos.guardarComo(
            QFileDialog(),
            self.editor.textEdit,
            self
        )
        if aux != self.ruta:
            self.titulo = f"Editor de texto - {self.ruta}"
            self.control = 0


    def validar(self, parametro):
        if self.control:
            msgbox = QMessageBox()
            msgbox.setWindowTitle("Alerta")
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            btnSi = msgbox.button(QMessageBox.Yes).setText("Si")
            if parametro == 1:
                msgbox.setText("Estás por crear un nuevo archivo, se va a eliminar el contenido modificado, ¿desea continuar?")
            elif parametro == 2:
                msgbox.setText("Estás por abrir otro archivo, se va a eliminar el contenido modificado, ¿desea continuar?")
            elif parametro == 3:
                msgbox.setText("Estás por cerrar el programa sin guardar cambios, ¿desea continuar?")
            respuesta = msgbox.exec_()
            if respuesta == QMessageBox.Yes:
                return 1
            else:
                return 0
        else:
            return 1

    def closeEvent(self, event: QCloseEvent):
        control = self.validar(3)
        if control:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_aplicacion = Editor()
    mi_aplicacion.show()
    sys.exit(app.exec_())
