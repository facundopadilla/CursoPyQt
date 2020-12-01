from PyQt5.QtWidgets import *
from ui2_primera import Ui_Form
import sys

click = 0

class Contador(QDialog):

    def __init__(self):
        super(Contador, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.btnClick.clicked.connect(self.sumador)

    def sumador(self):
        global click
        click += 1
        self.ui.contador.setText(str(click))

# --- Forma 2 ---

if __name__ == "__main__":
    app = QApplication([])
    mi_aplicacion = Contador()
    mi_aplicacion.show() # muestro la app
    sys.exit(app.exec_())
