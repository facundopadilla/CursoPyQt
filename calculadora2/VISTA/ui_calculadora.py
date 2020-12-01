# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
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


class Ui_Calculadora(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(344, 388)
        Form.setMinimumSize(QSize(0, 0))
        Form.setMaximumSize(QSize(344, 388))
        Form.setFocusPolicy(Qt.StrongFocus)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.contenedor = QFrame(Form)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setFocusPolicy(Qt.StrongFocus)
        self.contenedor.setFrameShape(QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.contenedor)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frameVisor = QFrame(self.contenedor)
        self.frameVisor.setObjectName(u"frameVisor")
        self.frameVisor.setFrameShape(QFrame.NoFrame)
        self.frameVisor.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frameVisor)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frameVisor)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frameVisor)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit.setAlignment(Qt.AlignRight)

        self.gridLayout_3.addWidget(self.lineEdit, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameVisor, 0, 0, 1, 1)

        self.frameBotones = QFrame(self.contenedor)
        self.frameBotones.setObjectName(u"frameBotones")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameBotones.sizePolicy().hasHeightForWidth())
        self.frameBotones.setSizePolicy(sizePolicy)
        self.frameBotones.setFrameShape(QFrame.NoFrame)
        self.frameBotones.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frameBotones)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btnMultiplicar = QPushButton(self.frameBotones)
        self.btnMultiplicar.setObjectName(u"btnMultiplicar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnMultiplicar.sizePolicy().hasHeightForWidth())
        self.btnMultiplicar.setSizePolicy(sizePolicy1)
        self.btnMultiplicar.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btnMultiplicar, 0, 3, 1, 1)

        self.btnPC = QPushButton(self.frameBotones)
        self.btnPC.setObjectName(u"btnPC")
        sizePolicy1.setHeightForWidth(self.btnPC.sizePolicy().hasHeightForWidth())
        self.btnPC.setSizePolicy(sizePolicy1)
        self.btnPC.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btnPC, 0, 2, 1, 1)

        self.btnC = QPushButton(self.frameBotones)
        self.btnC.setObjectName(u"btnC")
        sizePolicy1.setHeightForWidth(self.btnC.sizePolicy().hasHeightForWidth())
        self.btnC.setSizePolicy(sizePolicy1)
        self.btnC.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btnC, 0, 0, 1, 1)

        self.btn7 = QPushButton(self.frameBotones)
        self.btn7.setObjectName(u"btn7")
        sizePolicy1.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy1)
        self.btn7.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btn7, 1, 0, 1, 1)

        self.btn4 = QPushButton(self.frameBotones)
        self.btn4.setObjectName(u"btn4")
        sizePolicy1.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy1)
        self.btn4.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btn4, 2, 0, 1, 1)

        self.btnPA = QPushButton(self.frameBotones)
        self.btnPA.setObjectName(u"btnPA")
        sizePolicy1.setHeightForWidth(self.btnPA.sizePolicy().hasHeightForWidth())
        self.btnPA.setSizePolicy(sizePolicy1)
        self.btnPA.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btnPA, 0, 1, 1, 1)

        self.btn1 = QPushButton(self.frameBotones)
        self.btn1.setObjectName(u"btn1")
        sizePolicy1.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy1)
        self.btn1.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btn1, 3, 0, 1, 1)

        self.btnPunto = QPushButton(self.frameBotones)
        self.btnPunto.setObjectName(u"btnPunto")
        sizePolicy1.setHeightForWidth(self.btnPunto.sizePolicy().hasHeightForWidth())
        self.btnPunto.setSizePolicy(sizePolicy1)
        self.btnPunto.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btnPunto, 4, 0, 1, 1)

        self.btn8 = QPushButton(self.frameBotones)
        self.btn8.setObjectName(u"btn8")
        sizePolicy1.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy1)
        self.btn8.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btn8, 1, 1, 1, 1)

        self.btn9 = QPushButton(self.frameBotones)
        self.btn9.setObjectName(u"btn9")
        sizePolicy1.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy1)
        self.btn9.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btn9, 1, 2, 1, 1)

        self.btnDividir = QPushButton(self.frameBotones)
        self.btnDividir.setObjectName(u"btnDividir")
        sizePolicy1.setHeightForWidth(self.btnDividir.sizePolicy().hasHeightForWidth())
        self.btnDividir.setSizePolicy(sizePolicy1)
        self.btnDividir.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btnDividir, 1, 3, 1, 1)

        self.btn5 = QPushButton(self.frameBotones)
        self.btn5.setObjectName(u"btn5")
        sizePolicy1.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy1)
        self.btn5.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btn5, 2, 1, 1, 1)

        self.btn6 = QPushButton(self.frameBotones)
        self.btn6.setObjectName(u"btn6")
        sizePolicy1.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy1)
        self.btn6.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btn6, 2, 2, 1, 1)

        self.btnRestar = QPushButton(self.frameBotones)
        self.btnRestar.setObjectName(u"btnRestar")
        sizePolicy1.setHeightForWidth(self.btnRestar.sizePolicy().hasHeightForWidth())
        self.btnRestar.setSizePolicy(sizePolicy1)
        self.btnRestar.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btnRestar, 2, 3, 1, 1)

        self.btn2 = QPushButton(self.frameBotones)
        self.btn2.setObjectName(u"btn2")
        sizePolicy1.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy1)
        self.btn2.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btn2, 3, 1, 1, 1)

        self.btn3 = QPushButton(self.frameBotones)
        self.btn3.setObjectName(u"btn3")
        sizePolicy1.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy1)
        self.btn3.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btn3, 3, 2, 1, 1)

        self.btnSumar = QPushButton(self.frameBotones)
        self.btnSumar.setObjectName(u"btnSumar")
        sizePolicy1.setHeightForWidth(self.btnSumar.sizePolicy().hasHeightForWidth())
        self.btnSumar.setSizePolicy(sizePolicy1)
        self.btnSumar.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btnSumar, 3, 3, 1, 1)

        self.btn0 = QPushButton(self.frameBotones)
        self.btn0.setObjectName(u"btn0")
        sizePolicy1.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy1)
        self.btn0.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btn0, 4, 1, 1, 1)

        self.btnIgual = QPushButton(self.frameBotones)
        self.btnIgual.setObjectName(u"btnIgual")
        sizePolicy1.setHeightForWidth(self.btnIgual.sizePolicy().hasHeightForWidth())
        self.btnIgual.setSizePolicy(sizePolicy1)
        self.btnIgual.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_4.addWidget(self.btnIgual, 4, 2, 1, 2)


        self.gridLayout_2.addWidget(self.frameBotones, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.contenedor, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Calculadora", None))
        self.label.setText(QCoreApplication.translate("Form", u"CalculadoraQT", None))
        self.btnMultiplicar.setText(QCoreApplication.translate("Form", u"*", None))
        self.btnPC.setText(QCoreApplication.translate("Form", u")", None))
        self.btnC.setText(QCoreApplication.translate("Form", u"C", None))
        self.btn7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btnPA.setText(QCoreApplication.translate("Form", u"(", None))
        self.btn1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btnPunto.setText(QCoreApplication.translate("Form", u".", None))
        self.btn8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btn9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btnDividir.setText(QCoreApplication.translate("Form", u"%", None))
        self.btn5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btnRestar.setText(QCoreApplication.translate("Form", u"-", None))
        self.btn2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btnSumar.setText(QCoreApplication.translate("Form", u"+", None))
        self.btn0.setText(QCoreApplication.translate("Form", u"0", None))
        self.btnIgual.setText(QCoreApplication.translate("Form", u"=", None))
    # retranslateUi
