# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Ventana1(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(315, 320)
        self.lblUno = QLabel(Form)
        self.lblUno.setObjectName(u"lblUno")
        self.lblUno.setGeometry(QRect(90, 20, 101, 19))
        self.lineUno = QLineEdit(Form)
        self.lineUno.setObjectName(u"lineUno")
        self.lineUno.setGeometry(QRect(60, 80, 181, 25))
        self.btnUno = QPushButton(Form)
        self.btnUno.setObjectName(u"btnUno")
        self.btnUno.setGeometry(QRect(70, 110, 161, 34))
        self.btnAbrir = QPushButton(Form)
        self.btnAbrir.setObjectName(u"btnAbrir")
        self.btnAbrir.setGeometry(QRect(70, 260, 171, 34))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblUno.setText(QCoreApplication.translate("Form", u"Soy el label 1", None))
        self.lineUno.setPlaceholderText(QCoreApplication.translate("Form", u"Soy el LineEdit 1", None))
        self.btnUno.setText(QCoreApplication.translate("Form", u"Enviar informaci\u00f3n", None))
        self.btnAbrir.setText(QCoreApplication.translate("Form", u"Abrir ventana 2", None))
    # retranslateUi
