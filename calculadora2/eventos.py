def teclas(tecla, label, line):
    texto = label.text()
    if 40 <= tecla.key() <= 57:
        label.setText(texto + tecla.text())
    elif 16777220 <= tecla.key() <= 16777221: # enter
        if line.text() != "":
            line.clear()
        try:
            line.insert(str(eval(texto)))
        except:
            line.insert("Error: verifique la operación ingresada")
    elif tecla.key() == 16777219:
        label.setText(texto[:-1])
