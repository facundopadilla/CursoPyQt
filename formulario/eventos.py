import re

control = [None for i in range(4)] # [None, None, None, None]

def validarTexto(line_edit):
    if line_edit.text().isalpha() or " " in line_edit.text():
        line_edit.setStyleSheet("border: 1px solid green")
        control[0] = True
    else:
        line_edit.setStyleSheet("border: 1px solid red")
        control[0] = False

def validarNumero(line_edit):
    if (re.search("(?<=[a-zA-Z])", line_edit.text()) is None) and (re.search("[+*]|[-*]|[0-9]", line_edit.text()) is not None):
        line_edit.setStyleSheet("border: 1px solid green")
        control[1] = True
    else:
        line_edit.setStyleSheet("border: 1px solid red")
        control[1] = False

def validarDireccion(line_edit):
    if line_edit.text().isalnum() or " " in line_edit.text():
        line_edit.setStyleSheet("border: 1px solid green")
        control[2] = True
    else:
        line_edit.setStyleSheet("border: 1px solid red")
        control[2] = False

def validarEdad(spin):
    if spin.value() < 18:
        spin.setStyleSheet("border: 1px solid red")
        control[3] = False
    elif spin.value() >= 18:
        spin.setStyleSheet("border: 1px solid green")
        control[3] = True

def validarRegistro(objetos):
    if control.count(True) == 4:
        objetos[5].resultado = 1
    else:
        objetos[5].resultado = 2
