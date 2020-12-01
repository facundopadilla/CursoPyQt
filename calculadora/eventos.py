def teclas(tecla, label, line):
    texto = label.text()
    if (40 <= tecla.key() <= 57):
        label.setText(texto + str(tecla.text()))
    elif tecla.key() == 16777219:
        label.setText(texto[:-1])
    elif 16777220 <= tecla.key() <= 16777221:
        if line.text() != "":
            line.clear()
        try:
            line.insert(str(eval(texto)))
        except:
            line.insert("Error")
