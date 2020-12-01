from PySide2.QtWidgets import *
from ui_tateti import Ui_Tateti
import sys

class Tateti(QDialog):

    def __init__(self):
        super(Tateti, self).__init__()
        self.tateti = Ui_Tateti()
        self.tateti.setupUi(self)
        self.jugador = 1
        self.contador = 0

        # --- Matriz ---
        self.matriz = [[None, None, None], [None, None, None],[None, None, None]] # matriz de 3x3

        # --- Button: clicked ---
        self.tateti.btn1.clicked.connect(lambda: self.btnClicked([0,0], self.tateti.btn1))
        self.tateti.btn2.clicked.connect(lambda: self.btnClicked([0,1], self.tateti.btn2))
        self.tateti.btn3.clicked.connect(lambda: self.btnClicked([0,2], self.tateti.btn3))
        self.tateti.btn4.clicked.connect(lambda: self.btnClicked([1,0], self.tateti.btn4))
        self.tateti.btn5.clicked.connect(lambda: self.btnClicked([1,1], self.tateti.btn5))
        self.tateti.btn6.clicked.connect(lambda: self.btnClicked([1,2], self.tateti.btn6))
        self.tateti.btn7.clicked.connect(lambda: self.btnClicked([2,0], self.tateti.btn7))
        self.tateti.btn8.clicked.connect(lambda: self.btnClicked([2,1], self.tateti.btn8))
        self.tateti.btn9.clicked.connect(lambda: self.btnClicked([2,2], self.tateti.btn9))
        self.tateti.btnReiniciar.clicked.connect(lambda: self.reiniciar())

    """ def btnClicked
    - posición: es una lista con 2 elementos que corresponden a la posición de cada botón en self.matriz
    - botón: es el objeto que pasamos por referencia
    """

    def btnClicked(self, posicion, boton):
        if self.jugador == 1:
            self.matriz[posicion[0]][posicion[1]] = "x" # modifico el None de dicha posición por la X
            boton.setText("x") # modifico el texto del botón a la letra X
            self.jugador = 0 # cambio de turno de jugador (jugador 0 es el que usa la O)
        else:
            self.matriz[posicion[0]][posicion[1]] = "o" # modifico el None de dicha posición por la O
            boton.setText("o") # modifico el texto del botón a la letra O
            self.jugador = 1 # cambio de turno de jugador (jugador 1 es el que usa la X)
        self.contador += 1 # contador para evaluar el empate
        boton.setEnabled(False) # cada vez que se hace click en un botón, se desactiva para no poder ser modificado
        self.control() # controlamos si hay un ganador
        print(self.matriz) # es opcional, simplemente para que se vea la matriz

    def control(self):
        # --- Filas y columnas en X ---
        if((self.matriz[0][0] == "x" and self.matriz[0][1] == "x" and self.matriz[0][2] == "x") # fila 1 completa de X
        or (self.matriz[1][0] == "x" and self.matriz[1][1] == "x" and self.matriz[1][2] == "x") # fila 2 completa de X
        or (self.matriz[2][0] == "x" and self.matriz[2][1] == "x" and self.matriz[2][2] == "x") # fila 3 completa de X
        or (self.matriz[0][0] == "x" and self.matriz[1][0] == "x" and self.matriz[2][0] == "x") # columna 1 completa de X
        or (self.matriz[0][1] == "x" and self.matriz[1][1] == "x" and self.matriz[2][1] == "x") # columna 2 completa de X
        or (self.matriz[0][2] == "x" and self.matriz[1][2] == "x" and self.matriz[2][2] == "x") # columna 3 completa de X
        or (self.matriz[0][0] == "x" and self.matriz[1][1] == "x" and self.matriz[2][2] == "x") # diagonal de izquierda a derecha de X
        or (self.matriz[0][2] == "x" and self.matriz[1][1] == "x" and self.matriz[2][0] == "x")): # diagonal de derecha a izquierda de X
            print("Ganador: jugador 1") # muestro el ganador por consola/terminal
            self.ganador(1) # envío el ganador

        # -- Filas y columnas en O ---
        elif((self.matriz[0][0] == "o" and self.matriz[0][1] == "o" and self.matriz[0][2] == "o") # fila 1 completa de O
        or (self.matriz[1][0] == "o" and self.matriz[1][1] == "o" and self.matriz[1][2] == "o") # fila 2 completa de O
        or (self.matriz[2][0] == "o" and self.matriz[2][1] == "o" and self.matriz[2][2] == "o") # fila 3 completa de O
        or (self.matriz[0][0] == "o" and self.matriz[1][0] == "o" and self.matriz[2][0] == "o") # columna 1 completa de O
        or (self.matriz[0][1] == "o" and self.matriz[1][1] == "o" and self.matriz[2][1] == "o") # columna 2 completa de O
        or (self.matriz[0][2] == "o" and self.matriz[1][2] == "o" and self.matriz[2][2] == "o") # columna 3 completa de O
        or (self.matriz[0][0] == "o" and self.matriz[1][1] == "o" and self.matriz[2][2] == "o") # diagonal de izquierda a derecha de O
        or (self.matriz[0][2] == "o" and self.matriz[1][1] == "o" and self.matriz[2][0] == "o")): # diagonal de derecha a izquierda de O
            print("Ganador: jugador 2") # muestro el ganador por consola/terminal
            self.ganador(2)

        # -- Si nadie gana --
        elif self.contador == 9:
            print("Empate, nadie gana.") # muestro el empate por consola/terminal
            self.ganador(3) # envío el empate

    def ganador(self, ganador):
        msgbox = QMessageBox() # creo una ventana
        if 1 <= ganador <= 2: # evaluo si el ganador es el 1 o el 2
            msgbox.setWindowTitle("Ganador!") # le añado un título a la ventana
            msgbox.setText(f"El ganador es el jugador número: {ganador}") # le añado un texto a la ventana
        else:
            msgbox.setWindowTitle("Empate") # le añado un título a la ventana
            msgbox.setText("Ninguno ganó la ronda") # le añado un texto a la ventana
        msgbox.exec_() # ejecuto la ventana

    def reiniciar(self):
        # reinicio todo de vuelta como por defecto.
        self.matriz = [[None, None, None], [None, None, None],[None, None, None]]
        self.tateti.btn1.setText("")
        self.tateti.btn1.setEnabled(True)
        self.tateti.btn2.setText("")
        self.tateti.btn2.setEnabled(True)
        self.tateti.btn3.setText("")
        self.tateti.btn3.setEnabled(True)
        self.tateti.btn4.setText("")
        self.tateti.btn4.setEnabled(True)
        self.tateti.btn5.setText("")
        self.tateti.btn5.setEnabled(True)
        self.tateti.btn6.setText("")
        self.tateti.btn6.setEnabled(True)
        self.tateti.btn7.setText("")
        self.tateti.btn7.setEnabled(True)
        self.tateti.btn8.setText("")
        self.tateti.btn8.setEnabled(True)
        self.tateti.btn9.setText("")
        self.tateti.btn9.setEnabled(True)
        self.jugador = 1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mi_aplicacion = Tateti()
    mi_aplicacion.show()
    sys.exit(app.exec_())
