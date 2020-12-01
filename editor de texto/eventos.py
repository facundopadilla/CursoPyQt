def abrirArchivo(file_dialog, textEdit, editor):
    ruta = file_dialog.getOpenFileName(None, "Selecciona un archivo", "", "Python (*.py);;Texto (*.txt)")
    if ruta[0] != '':
        with open(ruta[0], "r", encoding='utf-8') as contenido:
            textEdit.setText(("").join(contenido.readlines()))
        editor.setWindowTitle("Editor de texto - " + ruta[0])
        return ruta[0]

def guardarComo(file_dialog, textEdit, editor):
    ruta = file_dialog.getSaveFileName(None, "Guardar archivo", "", "Python (*.py);;Texto (*.txt)")
    if ruta[0] != '':
        with open(ruta[0], "w", encoding='utf-8') as nuevo_archivo:
            nuevo_archivo.write(textEdit.toPlainText())
        editor.setWindowTitle("Editor de texto - " + ruta[0])
