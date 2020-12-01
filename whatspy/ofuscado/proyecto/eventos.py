from PySide2.QtWidgets import QTableWidgetItem, QFileDialog

from pandas import DataFrame
import xlwt

def maximizarVentana(programa):
    programa.showMaximized()

def normalizarVentana(programa):
    programa.showNormal()

def minimizarVentana(programa):
    programa.showMinimized()

def cerrarVentana(programa):
    programa.close()

def abrirChat(tabla, btnExportar, mensajeApp):
    ruta = QFileDialog.getOpenFileName(None, "Selecciona un archivo", "", "Chat WhatsApp (*.txt)")
    if ruta[0] != "":
        chat = ruta[0]
        df_chat = open(chat, 'r', encoding="utf-8").readlines()
        numeros = []
        for i in range(3, len(df_chat)):
            numero = ""
            mensaje = df_chat[i].split()
            for j in range(3, len(mensaje)):
                if (
                ("+" in mensaje[j]) or
                (mensaje[j].isnumeric()) or
                ("-" in mensaje[j]) or
                (":" in mensaje[j])
                ):
                    numero += mensaje[j]
            if ((":" in numero) and ("+" in numero) and ("-" in numero)):
                numero = numero.replace(numero[numero.index(":"):], "")
                numero = numero.replace(":","")
                numeros.append(numero)
        sin_repetidos = []
        for i in numeros:
            if i not in sin_repetidos:
                sin_repetidos.append(i)
        valores = []
        for i in sin_repetidos:
            valores.append([i, numeros.count(i)])
        for i in range(0, len(sin_repetidos)-1):
            for j in range(1, len(sin_repetidos)):
                if valores[i][1] > valores[j][1]:
                    aux = valores[j]
                    valores[j] = valores[i]
                    valores[i] = aux
        if valores[0][1] < valores[1][1]:
            valores.append(valores[0])
            valores.pop(0)
        filas_numeros = [valores[i][0] for i in range(len(valores))]
        filas_valores = [valores[i][1] for i in range(len(valores))]
        tabla.setRowCount(len(filas_numeros))
        for fila in range(len(filas_numeros)):
            tabla.setItem(fila, 0, QTableWidgetItem(str(filas_numeros[fila])))
            tabla.setItem(fila, 1, QTableWidgetItem(str(filas_valores[fila])))
        btnExportar.setEnabled(True)
        mensajeApp.setText(f"Archivo: {ruta[0]}")
        return [filas_numeros, filas_valores]

def exportarChat(filas_numeros, filas_valores):
    ruta_de_guardado = QFileDialog.getSaveFileName(None, "Guardar como...", "", "CSV (*.csv);;Excel (*.xls);;JSON (*.json);;HTML (*.html)")
    df_numeros = {"Números":filas_numeros,
                    "Cantidad de mensajes":filas_valores}
    df_numeros = DataFrame(df_numeros)
    if ruta_de_guardado != "":
        if ruta_de_guardado[1] == "CSV (*.csv)":
            df_numeros.to_csv(ruta_de_guardado[0])
        elif ruta_de_guardado[1] == "Excel (*.xls)":
            df_numeros.to_excel(ruta_de_guardado[0])
        elif ruta_de_guardado[1] == "JSON (*.json)":
            df_numeros.to_json(ruta_de_guardado[0])
        elif ruta_de_guardado[1] == "HTML (*.html)":
            df_numeros.to_html(ruta_de_guardado[0])
    