# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'primera_app.ui'
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

from images import source2

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 320)
        self.titulo = QLabel(Form)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(60, 10, 131, 19))
        self.contador = QLabel(Form)
        self.contador.setObjectName(u"contador")
        self.contador.setGeometry(QRect(60, 40, 121, 71))
        font = QFont()
        font.setFamily(u"MS PGothic")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.contador.setFont(font)
        self.contador.setFrameShape(QFrame.Box)
        self.contador.setAlignment(Qt.AlignCenter)
        self.btnClick = QPushButton(Form)
        self.btnClick.setObjectName(u"btnClick")
        self.btnClick.setGeometry(QRect(60, 130, 112, 34))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 180, 91, 81))
        self.label_3.setPixmap(QPixmap(u":/images/cocacola.jpg"))
        self.label_3.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Contador de clicks", None))
        self.titulo.setText(QCoreApplication.translate("Form", u"Contador de clicks", None))
        self.contador.setText(QCoreApplication.translate("Form", u"0", None))
        self.btnClick.setText(QCoreApplication.translate("Form", u"Haz click aqu\u00ed", None))
        self.label_3.setText("")
    # retranslateUi

