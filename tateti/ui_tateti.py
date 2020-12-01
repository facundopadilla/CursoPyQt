# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tateti.ui'
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


class Ui_Tateti(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(277, 311)
        self.Titulo = QLabel(Form)
        self.Titulo.setObjectName(u"Titulo")
        self.Titulo.setGeometry(QRect(80, 10, 131, 19))
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(50, 150, 191, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(50, 90, 191, 16))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(100, 50, 20, 161))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.line_4 = QFrame(Form)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(170, 50, 20, 161))
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)
        self.btnReiniciar = QPushButton(Form)
        self.btnReiniciar.setObjectName(u"btnReiniciar")
        self.btnReiniciar.setGeometry(QRect(70, 250, 141, 34))
        self.btnReiniciar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn1 = QPushButton(Form)
        self.btn1.setObjectName(u"btn1")
        self.btn1.setGeometry(QRect(50, 50, 51, 41))
        self.btn1.setFlat(True)
        self.btn2 = QPushButton(Form)
        self.btn2.setObjectName(u"btn2")
        self.btn2.setGeometry(QRect(120, 50, 51, 41))
        self.btn2.setFlat(True)
        self.btn3 = QPushButton(Form)
        self.btn3.setObjectName(u"btn3")
        self.btn3.setGeometry(QRect(190, 50, 51, 41))
        self.btn3.setFlat(True)
        self.btn4 = QPushButton(Form)
        self.btn4.setObjectName(u"btn4")
        self.btn4.setGeometry(QRect(50, 110, 51, 41))
        self.btn4.setFlat(True)
        self.btn5 = QPushButton(Form)
        self.btn5.setObjectName(u"btn5")
        self.btn5.setGeometry(QRect(120, 110, 51, 41))
        self.btn5.setFlat(True)
        self.btn6 = QPushButton(Form)
        self.btn6.setObjectName(u"btn6")
        self.btn6.setGeometry(QRect(190, 110, 51, 41))
        self.btn6.setFlat(True)
        self.btn7 = QPushButton(Form)
        self.btn7.setObjectName(u"btn7")
        self.btn7.setGeometry(QRect(50, 160, 51, 41))
        self.btn7.setFlat(True)
        self.btn8 = QPushButton(Form)
        self.btn8.setObjectName(u"btn8")
        self.btn8.setGeometry(QRect(120, 160, 51, 41))
        self.btn8.setFlat(True)
        self.btn9 = QPushButton(Form)
        self.btn9.setObjectName(u"btn9")
        self.btn9.setGeometry(QRect(190, 160, 51, 41))
        self.btn9.setFlat(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Titulo.setText(QCoreApplication.translate("Form", u"Juego del TaTeTi", None))
        self.btnReiniciar.setText(QCoreApplication.translate("Form", u"Reiniciar juego", None))
        self.btn1.setText("")
        self.btn2.setText("")
        self.btn3.setText("")
        self.btn4.setText("")
        self.btn5.setText("")
        self.btn6.setText("")
        self.btn7.setText("")
        self.btn8.setText("")
        self.btn9.setText("")
    # retranslateUi
