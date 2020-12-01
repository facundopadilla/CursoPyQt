from PyQt5.QtWidgets import *
from VISTA.ui_tablas import Ui_Form
from MODELO.cargar_tablas import cargarTableWidget, cargarTableView

import sys, eventos

class Ejercicio(QDialog):

    def __init__(self):
        super(Ejercicio, self).__init__()
        self.ejercicio = Ui_Form()
        self.ejercicio.setupUi(self)

        # --- Cargar tablas ---
        cargarTableWidget(self.ejercicio.tableWidget)
        cargarTableView(self.ejercicio.tableView)

        # --- Eventos ---
        self.ejercicio.tableWidget.cellDoubleClicked.connect(self.tableWidgetDoubleClicked)
        self.ejercicio.tableView.doubleClicked.connect(self.tableViewDoubleClicked)

    def tableWidgetDoubleClicked(self, fila):
        eventos.enviar_a_view(fila, self.ejercicio.tableWidget, self.ejercicio.tableView)

    def tableViewDoubleClicked(self, item):
        eventos.enviar_a_widget(item.row(), self.ejercicio.tableWidget, self.ejercicio.tableView)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_aplicacion = Ejercicio()
    mi_aplicacion.show()
    sys.exit(app.exec_())
