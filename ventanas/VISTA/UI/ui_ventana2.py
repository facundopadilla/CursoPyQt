# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana2.ui'
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


class Ui_Ventana2(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(352, 320)
        self.lblDos = QLabel(Form)
        self.lblDos.setObjectName(u"lblDos")
        self.lblDos.setGeometry(QRect(130, 20, 101, 19))
        self.lineDos = QLineEdit(Form)
        self.lineDos.setObjectName(u"lineDos")
        self.lineDos.setGeometry(QRect(100, 80, 181, 25))
        self.btnDos = QPushButton(Form)
        self.btnDos.setObjectName(u"btnDos")
        self.btnDos.setGeometry(QRect(110, 130, 161, 34))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lblDos.setText(QCoreApplication.translate("Form", u"Soy el label 2", None))
        self.lineDos.setText("")
        self.lineDos.setPlaceholderText(QCoreApplication.translate("Form", u"Soy el LineEdit 2", None))
        self.btnDos.setText(QCoreApplication.translate("Form", u"Enviar informaci\u00f3n", None))
    # retranslateUi
