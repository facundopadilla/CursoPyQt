# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventanaAdd.ui'
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


class Ui_VentanaAdd(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(449, 296)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 5)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lblNombre = QLabel(self.frame)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lblNombre)

        self.lineNombre = QLineEdit(self.frame)
        self.lineNombre.setObjectName(u"lineNombre")
        self.lineNombre.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineNombre)

        self.lblApellido = QLabel(self.frame)
        self.lblApellido.setObjectName(u"lblApellido")
        self.lblApellido.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.lblApellido)

        self.lineApellido = QLineEdit(self.frame)
        self.lineApellido.setObjectName(u"lineApellido")
        self.lineApellido.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineApellido)

        self.lblDni = QLabel(self.frame)
        self.lblDni.setObjectName(u"lblDni")
        self.lblDni.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lblDni)

        self.lineDni = QLineEdit(self.frame)
        self.lineDni.setObjectName(u"lineDni")
        self.lineDni.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineDni)

        self.lblDireccion = QLabel(self.frame)
        self.lblDireccion.setObjectName(u"lblDireccion")
        self.lblDireccion.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.lblDireccion)

        self.lineDireccion = QLineEdit(self.frame)
        self.lineDireccion.setObjectName(u"lineDireccion")
        self.lineDireccion.setClearButtonEnabled(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.lineDireccion)

        self.lblTelefono = QLabel(self.frame)
        self.lblTelefono.setObjectName(u"lblTelefono")
        self.lblTelefono.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lblTelefono)

        self.lineTel = QLineEdit(self.frame)
        self.lineTel.setObjectName(u"lineTel")
        self.lineTel.setClearButtonEnabled(True)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.lineTel)

        self.btnBuscarFoto = QPushButton(self.frame)
        self.btnBuscarFoto.setObjectName(u"btnBuscarFoto")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.btnBuscarFoto)

        self.lineFoto = QLineEdit(self.frame)
        self.lineFoto.setObjectName(u"lineFoto")
        self.lineFoto.setClearButtonEnabled(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lineFoto)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 0, 2, 0)
        self.btnAdd = QPushButton(self.frame_2)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setMinimumSize(QSize(0, 20))

        self.gridLayout_2.addWidget(self.btnAdd, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"A\u00f1adir persona", None))
        self.lblNombre.setText(QCoreApplication.translate("Form", u"Ingresar nombre", None))
        self.lineNombre.setPlaceholderText(QCoreApplication.translate("Form", u"Ingresar nombre", None))
        self.lblApellido.setText(QCoreApplication.translate("Form", u"Ingresar apellido", None))
        self.lineApellido.setPlaceholderText(QCoreApplication.translate("Form", u"Ingresar apellidos", None))
        self.lblDni.setText(QCoreApplication.translate("Form", u"Ingresar DNI", None))
        self.lineDni.setPlaceholderText(QCoreApplication.translate("Form", u"Ingresar DNI", None))
        self.lblDireccion.setText(QCoreApplication.translate("Form", u"Ingresar direcci\u00f3n", None))
        self.lineDireccion.setPlaceholderText(QCoreApplication.translate("Form", u"Ingresar direcci\u00f3n", None))
        self.lblTelefono.setText(QCoreApplication.translate("Form", u"Ingresar tel\u00e9fono", None))
        self.lineTel.setPlaceholderText(QCoreApplication.translate("Form", u"Ingresar tel\u00e9fono", None))
        self.btnBuscarFoto.setText(QCoreApplication.translate("Form", u"Buscar foto", None))
        self.lineFoto.setPlaceholderText(QCoreApplication.translate("Form", u"...", None))
        self.btnAdd.setText(QCoreApplication.translate("Form", u"A\u00f1adir nueva persona", None))
    # retranslateUi
