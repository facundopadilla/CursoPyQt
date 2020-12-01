# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'whatspy_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide2.QtGui import (QCursor, QFont, QIcon, QLinearGradient, QPixmap)
from PySide2.QtWidgets import QGridLayout, QFrame, QSizePolicy, QPushButton, QTableWidget, QTableWidgetItem, QSpacerItem, \
        QHBoxLayout, QLabel

from . import source

class Ui_Whatspy(object):
    def setupUi(self, Ventana):
        if not Ventana.objectName():
            Ventana.setObjectName(u"Ventana")
        Ventana.resize(424, 600)
        Ventana.setAttribute(Qt.WA_TranslucentBackground)
        Ventana.setWindowFlag(Qt.FramelessWindowHint)
        Ventana.setStyleSheet(u"*{\n"
"	font-family: century gothic;\n"
"}\n"
"\n"
"QSizeGrip{\n"
"       background: transparent;\n"
"}\n"
"\n"
"QLabel{\n"
"	color: white;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"            border: 1px solid #999999;\n"
"            width:12px;    \n"
"            margin: 0px 0px 0px 0px;\n"
"        }\n"
"        QScrollBar::handle:vertical {         \n"
"       \n"
"            min-height: 0px;\n"
"          	border: 0px solid red;\n"
"			border-radius: 4px;\n"
"			background-color: rgb(182, 182, 182);\n"
"        }\n"
"        QScrollBar::add-line:vertical {       \n"
"            height: 0px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"        QScrollBar::sub-line:vertical {\n"
"            height: 0 px;\n"
"            subcontrol-position: top;\n"
"            subcontrol-origin: margin;\n"
"        }")
        self.gridLayout = QGridLayout(Ventana)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.VentanaFrame = QFrame(Ventana)
        self.VentanaFrame.setObjectName(u"VentanaFrame")
        self.VentanaFrame.setStyleSheet(u"QFrame#VentanaFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0.953, y1:1, x2:1, y2:0, stop:0 	#075E54, stop:1 #128C7E);\n"
"	border-radius: 5px;\n"
"}")
        self.VentanaFrame.setFrameShape(QFrame.StyledPanel)
        self.VentanaFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.VentanaFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.Contenedor = QFrame(self.VentanaFrame)
        self.Contenedor.setObjectName(u"Contenedor")
        self.Contenedor.setStyleSheet(u"QFrame#Contenedor{\n"
"	background-color: #128C7E;\n"
"	border-radius: 5px;\n"
"}")
        self.Contenedor.setFrameShape(QFrame.StyledPanel)
        self.Contenedor.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.Contenedor)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 10, 0, 10)
        self.frameAcciones = QFrame(self.Contenedor)
        self.frameAcciones.setObjectName(u"frameAcciones")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameAcciones.sizePolicy().hasHeightForWidth())
        self.frameAcciones.setSizePolicy(sizePolicy)
        self.frameAcciones.setStyleSheet(u"")
        self.frameAcciones.setFrameShape(QFrame.StyledPanel)
        self.frameAcciones.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frameAcciones)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btnExportar = QPushButton(self.frameAcciones)
        self.btnExportar.setObjectName(u"btnExportar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnExportar.sizePolicy().hasHeightForWidth())
        self.btnExportar.setSizePolicy(sizePolicy1)
        self.btnExportar.setMinimumSize(QSize(100, 30))
        self.btnExportar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnExportar.setStyleSheet(u"QPushButton#btnExportar{\n"
"background-color: #ecf0f1;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btnExportar:hover{\n"
"background-color: #bdc3c7;\n"
"border-radius: 5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/logo/exportar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnExportar.setIcon(icon1)
        self.btnExportar.setIconSize(QSize(16, 16))

        self.gridLayout_4.addWidget(self.btnExportar, 0, 2, 1, 1)

        self.btnAbrir = QPushButton(self.frameAcciones)
        self.btnAbrir.setObjectName(u"btnAbrir")
        sizePolicy1.setHeightForWidth(self.btnAbrir.sizePolicy().hasHeightForWidth())
        self.btnAbrir.setSizePolicy(sizePolicy1)
        self.btnAbrir.setMinimumSize(QSize(100, 30))
        self.btnAbrir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAbrir.setStyleSheet(u"QPushButton#btnAbrir{\n"
"background-color: #ecf0f1;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btnAbrir:hover{\n"
"background-color: #bdc3c7;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/logo/anadir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnAbrir.setIcon(icon2)
        self.btnAbrir.setIconSize(QSize(16, 16))

        self.gridLayout_4.addWidget(self.btnAbrir, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.frameAcciones, 2, 0, 1, 1)

        self.frameTabla = QFrame(self.Contenedor)
        self.frameTabla.setObjectName(u"frameTabla")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frameTabla.sizePolicy().hasHeightForWidth())
        self.frameTabla.setSizePolicy(sizePolicy2)
        self.frameTabla.setStyleSheet(u"")
        self.frameTabla.setFrameShape(QFrame.StyledPanel)
        self.frameTabla.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frameTabla)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.tableWidget = QTableWidget(self.frameTabla)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 50):
            self.tableWidget.setRowCount(50)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy1.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy1)
        self.tableWidget.setMinimumSize(QSize(350, 0))
        self.tableWidget.setStyleSheet(u"QTableWidget#tableWidget:item{\n"
"color:white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QTableWidget#tableWidget{\n"
"border-radius:4px;\n"
"background-color: #128C7E;\n"
"}")
        self.tableWidget.setRowCount(50)

        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.gridLayout_5.addWidget(self.frameTabla, 3, 0, 1, 1)

        self.header = QFrame(self.Contenedor)
        self.header.setObjectName(u"header")
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setStyleSheet(u"")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 5, 0)
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnVerde = QPushButton(self.header)
        self.btnVerde.setObjectName(u"btnVerde")
        self.btnVerde.setMaximumSize(QSize(16, 16))
        self.btnVerde.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnVerde.setStyleSheet(u"QPushButton#btnVerde{\n"
"	background-color: #27ae60;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton#btnVerde:hover{\n"
"	background-color: #10ac84;\n"
"	border-radius: 8px;\n"
"}")

        self.horizontalLayout.addWidget(self.btnVerde)

        self.btnAmarillo = QPushButton(self.header)
        self.btnAmarillo.setObjectName(u"btnAmarillo")
        self.btnAmarillo.setMaximumSize(QSize(16, 16))
        self.btnAmarillo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnAmarillo.setStyleSheet(u"QPushButton#btnAmarillo{\n"
"background-color: yellow;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton#btnAmarillo:hover{\n"
"background-color: #f1c40f;\n"
"border-radius: 8px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btnAmarillo)

        self.btnRojo = QPushButton(self.header)
        self.btnRojo.setObjectName(u"btnRojo")
        self.btnRojo.setMaximumSize(QSize(16, 16))
        self.btnRojo.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnRojo.setStyleSheet(u"QPushButton#btnRojo{\n"
"background-color: red;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton#btnRojo:hover{\n"
"background-color: #e74c3c;\n"
"border-radius: 8px;\n"
"}")

        self.horizontalLayout.addWidget(self.btnRojo)


        self.gridLayout_5.addWidget(self.header, 0, 0, 1, 1)

        self.frameLogo = QFrame(self.Contenedor)
        self.frameLogo.setObjectName(u"frameLogo")
        sizePolicy.setHeightForWidth(self.frameLogo.sizePolicy().hasHeightForWidth())
        self.frameLogo.setSizePolicy(sizePolicy)
        self.frameLogo.setStyleSheet(u"")
        self.frameLogo.setFrameShape(QFrame.StyledPanel)
        self.frameLogo.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frameLogo)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lblWhatsPy = QLabel(self.frameLogo)
        self.lblWhatsPy.setObjectName(u"lblWhatsPy")
        font = QFont()
        font.setFamily(u"century gothic")
        font.setBold(True)
        font.setWeight(75)
        self.lblWhatsPy.setFont(font)
        self.lblWhatsPy.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblWhatsPy, 1, 0, 1, 1)

        self.icon = QLabel(self.frameLogo)
        self.icon.setObjectName(u"icon")
        self.icon.setMaximumSize(QSize(70, 70))
        self.icon.setPixmap(QPixmap(u":/logo/logo.png"))
        self.icon.setScaledContents(True)

        self.gridLayout_3.addWidget(self.icon, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frameLogo, 1, 0, 1, 1)

        self.label = QLabel(self.Contenedor)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.Contenedor, 0, 0, 1, 1)

        self.lblGrip = QLabel(self.VentanaFrame)
        self.lblGrip.setObjectName(u"lblGrip")
        sizePolicy.setHeightForWidth(self.lblGrip.sizePolicy().hasHeightForWidth())
        self.lblGrip.setSizePolicy(sizePolicy)
        self.lblGrip.setMaximumSize(QSize(10, 10))
        self.lblGrip.setCursor(QCursor(Qt.BusyCursor))
        self.lblGrip.setLayoutDirection(Qt.RightToLeft)
        self.lblGrip.setStyleSheet(u"QLabel#lblGrip:hover{\n"
"	background: rgb(18, 140, 126);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QLabel#lblGrip{\n"
"	background-color: qlineargradient(spread:pad, x1:0.953, y1:1, x2:1, y2:0, stop:0 	#075E54, stop:1 #128C7E);\n"
"	border-radius: 5px;\n"
"}")

        self.gridLayout_2.addWidget(self.lblGrip, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.VentanaFrame, 0, 0, 1, 1)


        self.retranslateUi(Ventana)

        QMetaObject.connectSlotsByName(Ventana)
    # setupUi

    def retranslateUi(self, Ventana):
        Ventana.setWindowTitle(QCoreApplication.translate("Ventana", u"Form", None))
        self.btnExportar.setText(QCoreApplication.translate("Ventana", u"Exportar", None))
        self.btnAbrir.setText(QCoreApplication.translate("Ventana", u"Abrir TXT", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Ventana", u"N\u00fameros", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Ventana", u"Mensajes", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.btnVerde.setText("")
        self.btnAmarillo.setText("")
        self.btnRojo.setText("")
        self.lblWhatsPy.setText(QCoreApplication.translate("Ventana", u"WhatsPy", None))
        self.icon.setText("")
        self.label.setText(QCoreApplication.translate("Ventana", u"Todav\u00eda no haz cargado ning\u00fan chat", None))
        self.lblGrip.setText("")
    # retranslateUi

