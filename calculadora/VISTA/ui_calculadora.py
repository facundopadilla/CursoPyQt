# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculadora.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_Calculadora(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(327, 386)
        Form.setMaximumSize(QSize(327, 386))
        Form.setFocusPolicy(Qt.StrongFocus)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFocusPolicy(Qt.StrongFocus)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(9)
        self.gridLayout_2.setContentsMargins(13, 13, 13, 13)
        self.frameVisor = QFrame(self.frame)
        self.frameVisor.setObjectName(u"frameVisor")
        self.frameVisor.setFrameShape(QFrame.NoFrame)
        self.frameVisor.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frameVisor)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(5)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frameVisor)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label.setIndent(1)
        self.label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.frameVisor)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setSizeIncrement(QSize(0, 0))
        self.lineEdit.setBaseSize(QSize(90, 90))
        font = QFont()
        font.setStyleStrategy(QFont.PreferDefault)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.lineEdit.setLayoutDirection(Qt.LeftToRight)
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)
        self.lineEdit.setClearButtonEnabled(False)

        self.gridLayout_4.addWidget(self.lineEdit, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frameVisor, 0, 0, 1, 1)

        self.frameBotones = QFrame(self.frame)
        self.frameBotones.setObjectName(u"frameBotones")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameBotones.sizePolicy().hasHeightForWidth())
        self.frameBotones.setSizePolicy(sizePolicy1)
        self.frameBotones.setFrameShape(QFrame.NoFrame)
        self.frameBotones.setFrameShadow(QFrame.Plain)
        self.frameBotones.setLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.frameBotones)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btnPA = QPushButton(self.frameBotones)
        self.btnPA.setObjectName(u"btnPA")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnPA.sizePolicy().hasHeightForWidth())
        self.btnPA.setSizePolicy(sizePolicy2)
        self.btnPA.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btnPA, 4, 4, 1, 1)

        self.btnC = QPushButton(self.frameBotones)
        self.btnC.setObjectName(u"btnC")
        sizePolicy2.setHeightForWidth(self.btnC.sizePolicy().hasHeightForWidth())
        self.btnC.setSizePolicy(sizePolicy2)
        self.btnC.setFocusPolicy(Qt.NoFocus)
        self.btnC.setFlat(False)

        self.gridLayout_3.addWidget(self.btnC, 4, 3, 1, 1)

        self.btnPC = QPushButton(self.frameBotones)
        self.btnPC.setObjectName(u"btnPC")
        sizePolicy2.setHeightForWidth(self.btnPC.sizePolicy().hasHeightForWidth())
        self.btnPC.setSizePolicy(sizePolicy2)
        self.btnPC.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btnPC, 4, 5, 1, 1)

        self.btnMultiplicar = QPushButton(self.frameBotones)
        self.btnMultiplicar.setObjectName(u"btnMultiplicar")
        sizePolicy2.setHeightForWidth(self.btnMultiplicar.sizePolicy().hasHeightForWidth())
        self.btnMultiplicar.setSizePolicy(sizePolicy2)
        self.btnMultiplicar.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btnMultiplicar, 4, 6, 1, 1)

        self.btn4 = QPushButton(self.frameBotones)
        self.btn4.setObjectName(u"btn4")
        sizePolicy2.setHeightForWidth(self.btn4.sizePolicy().hasHeightForWidth())
        self.btn4.setSizePolicy(sizePolicy2)
        self.btn4.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn4, 6, 3, 1, 1)

        self.btn7 = QPushButton(self.frameBotones)
        self.btn7.setObjectName(u"btn7")
        sizePolicy2.setHeightForWidth(self.btn7.sizePolicy().hasHeightForWidth())
        self.btn7.setSizePolicy(sizePolicy2)
        self.btn7.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn7, 5, 3, 1, 1)

        self.btn1 = QPushButton(self.frameBotones)
        self.btn1.setObjectName(u"btn1")
        sizePolicy2.setHeightForWidth(self.btn1.sizePolicy().hasHeightForWidth())
        self.btn1.setSizePolicy(sizePolicy2)
        self.btn1.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn1, 7, 3, 1, 1)

        self.btnSumar = QPushButton(self.frameBotones)
        self.btnSumar.setObjectName(u"btnSumar")
        sizePolicy2.setHeightForWidth(self.btnSumar.sizePolicy().hasHeightForWidth())
        self.btnSumar.setSizePolicy(sizePolicy2)
        self.btnSumar.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btnSumar, 7, 6, 1, 1)

        self.btn6 = QPushButton(self.frameBotones)
        self.btn6.setObjectName(u"btn6")
        sizePolicy2.setHeightForWidth(self.btn6.sizePolicy().hasHeightForWidth())
        self.btn6.setSizePolicy(sizePolicy2)
        self.btn6.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn6, 6, 5, 1, 1)

        self.btn2 = QPushButton(self.frameBotones)
        self.btn2.setObjectName(u"btn2")
        sizePolicy2.setHeightForWidth(self.btn2.sizePolicy().hasHeightForWidth())
        self.btn2.setSizePolicy(sizePolicy2)
        self.btn2.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn2, 7, 4, 1, 1)

        self.btn3 = QPushButton(self.frameBotones)
        self.btn3.setObjectName(u"btn3")
        sizePolicy2.setHeightForWidth(self.btn3.sizePolicy().hasHeightForWidth())
        self.btn3.setSizePolicy(sizePolicy2)
        self.btn3.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn3, 7, 5, 1, 1)

        self.btnRestar = QPushButton(self.frameBotones)
        self.btnRestar.setObjectName(u"btnRestar")
        sizePolicy2.setHeightForWidth(self.btnRestar.sizePolicy().hasHeightForWidth())
        self.btnRestar.setSizePolicy(sizePolicy2)
        self.btnRestar.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btnRestar, 6, 6, 1, 1)

        self.btn5 = QPushButton(self.frameBotones)
        self.btn5.setObjectName(u"btn5")
        sizePolicy2.setHeightForWidth(self.btn5.sizePolicy().hasHeightForWidth())
        self.btn5.setSizePolicy(sizePolicy2)
        self.btn5.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn5, 6, 4, 1, 1)

        self.btn8 = QPushButton(self.frameBotones)
        self.btn8.setObjectName(u"btn8")
        sizePolicy2.setHeightForWidth(self.btn8.sizePolicy().hasHeightForWidth())
        self.btn8.setSizePolicy(sizePolicy2)
        self.btn8.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn8, 5, 4, 1, 1)

        self.btnDividir = QPushButton(self.frameBotones)
        self.btnDividir.setObjectName(u"btnDividir")
        sizePolicy2.setHeightForWidth(self.btnDividir.sizePolicy().hasHeightForWidth())
        self.btnDividir.setSizePolicy(sizePolicy2)
        self.btnDividir.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btnDividir, 5, 6, 1, 1)

        self.btn9 = QPushButton(self.frameBotones)
        self.btn9.setObjectName(u"btn9")
        sizePolicy2.setHeightForWidth(self.btn9.sizePolicy().hasHeightForWidth())
        self.btn9.setSizePolicy(sizePolicy2)
        self.btn9.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn9, 5, 5, 1, 1)

        self.btnPunto = QPushButton(self.frameBotones)
        self.btnPunto.setObjectName(u"btnPunto")
        sizePolicy2.setHeightForWidth(self.btnPunto.sizePolicy().hasHeightForWidth())
        self.btnPunto.setSizePolicy(sizePolicy2)
        self.btnPunto.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btnPunto, 8, 3, 1, 1)

        self.btn0 = QPushButton(self.frameBotones)
        self.btn0.setObjectName(u"btn0")
        sizePolicy2.setHeightForWidth(self.btn0.sizePolicy().hasHeightForWidth())
        self.btn0.setSizePolicy(sizePolicy2)
        self.btn0.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btn0, 8, 4, 1, 1)

        self.btnIgual = QPushButton(self.frameBotones)
        self.btnIgual.setObjectName(u"btnIgual")
        sizePolicy2.setHeightForWidth(self.btnIgual.sizePolicy().hasHeightForWidth())
        self.btnIgual.setSizePolicy(sizePolicy2)
        self.btnIgual.setFocusPolicy(Qt.NoFocus)

        self.gridLayout_3.addWidget(self.btnIgual, 8, 5, 1, 2)


        self.gridLayout_2.addWidget(self.frameBotones, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"CalculadoraQT", None))
        self.btnPA.setText(QCoreApplication.translate("Form", u"(", None))
        self.btnC.setText(QCoreApplication.translate("Form", u"C", None))
        self.btnPC.setText(QCoreApplication.translate("Form", u")", None))
        self.btnMultiplicar.setText(QCoreApplication.translate("Form", u"*", None))
        self.btn4.setText(QCoreApplication.translate("Form", u"4", None))
        self.btn7.setText(QCoreApplication.translate("Form", u"7", None))
        self.btn1.setText(QCoreApplication.translate("Form", u"1", None))
        self.btnSumar.setText(QCoreApplication.translate("Form", u"+", None))
        self.btn6.setText(QCoreApplication.translate("Form", u"6", None))
        self.btn2.setText(QCoreApplication.translate("Form", u"2", None))
        self.btn3.setText(QCoreApplication.translate("Form", u"3", None))
        self.btnRestar.setText(QCoreApplication.translate("Form", u"-", None))
        self.btn5.setText(QCoreApplication.translate("Form", u"5", None))
        self.btn8.setText(QCoreApplication.translate("Form", u"8", None))
        self.btnDividir.setText(QCoreApplication.translate("Form", u"%", None))
        self.btn9.setText(QCoreApplication.translate("Form", u"9", None))
        self.btnPunto.setText(QCoreApplication.translate("Form", u".", None))
        self.btn0.setText(QCoreApplication.translate("Form", u"0", None))
        self.btnIgual.setText(QCoreApplication.translate("Form", u"=", None))
    # retranslateUi
