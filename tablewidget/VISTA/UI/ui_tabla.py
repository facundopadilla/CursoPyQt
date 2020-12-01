# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabla.ui'
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


class Ui_Tabla(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1069, 823)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnAdd = QPushButton(self.frame_2)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout.addWidget(self.btnAdd)

        self.btnEditar_2 = QPushButton(self.frame_2)
        self.btnEditar_2.setObjectName(u"btnEditar_2")

        self.horizontalLayout.addWidget(self.btnEditar_2)

        self.btnBuscar = QPushButton(self.frame_2)
        self.btnBuscar.setObjectName(u"btnBuscar")

        self.horizontalLayout.addWidget(self.btnBuscar)

        self.btnBorrar = QPushButton(self.frame_2)
        self.btnBorrar.setObjectName(u"btnBorrar")

        self.horizontalLayout.addWidget(self.btnBorrar)


        self.gridLayout_4.addWidget(self.frame_2, 0, 0, 1, 2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabla = QTableWidget(self.frame_3)
        if (self.tabla.columnCount() < 6):
            self.tabla.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tabla.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tabla.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.tabla.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.tabla.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.tabla.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tabla.rowCount() < 1):
            self.tabla.setRowCount(1)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.tabla.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.tabla.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.tabla.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.tabla.setItem(0, 3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.tabla.setItem(0, 4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.tabla.setItem(0, 5, __qtablewidgetitem12)
        self.tabla.setObjectName(u"tabla")
        self.tabla.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tabla.setSortingEnabled(False)
        self.tabla.horizontalHeader().setCascadingSectionResizes(False)

        self.gridLayout_2.addWidget(self.tabla, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_3, 1, 0, 2, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.gridLayout_3 = QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.lblNombre = QLabel(self.frame_5)
        self.lblNombre.setObjectName(u"lblNombre")
        self.lblNombre.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblNombre, 1, 0, 1, 1)

        self.lblDni = QLabel(self.frame_5)
        self.lblDni.setObjectName(u"lblDni")
        self.lblDni.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblDni, 3, 0, 1, 1)

        self.lblApellido = QLabel(self.frame_5)
        self.lblApellido.setObjectName(u"lblApellido")
        self.lblApellido.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblApellido, 2, 0, 1, 1)

        self.lblDireccion = QLabel(self.frame_5)
        self.lblDireccion.setObjectName(u"lblDireccion")
        self.lblDireccion.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblDireccion, 4, 0, 1, 1)

        self.lblTel = QLabel(self.frame_5)
        self.lblTel.setObjectName(u"lblTel")
        self.lblTel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblTel, 5, 0, 1, 1)

        self.lblFoto = QLabel(self.frame_5)
        self.lblFoto.setObjectName(u"lblFoto")
        self.lblFoto.setMinimumSize(QSize(120, 120))
        self.lblFoto.setMaximumSize(QSize(120, 120))
        self.lblFoto.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblFoto, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_5, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnAbrir = QPushButton(self.frame_4)
        self.btnAbrir.setObjectName(u"btnAbrir")

        self.verticalLayout.addWidget(self.btnAbrir)


        self.gridLayout_4.addWidget(self.frame_4, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Editor de personas", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.btnEditar_2.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.btnBuscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.btnBorrar.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        ___qtablewidgetitem = self.tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem1 = self.tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Apellido", None));
        ___qtablewidgetitem2 = self.tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"DNI", None));
        ___qtablewidgetitem3 = self.tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None));
        ___qtablewidgetitem4 = self.tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None));
        ___qtablewidgetitem5 = self.tabla.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Foto", None));
        ___qtablewidgetitem6 = self.tabla.verticalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"1", None));

        __sortingEnabled = self.tabla.isSortingEnabled()
        self.tabla.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.tabla.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Facundo", None));
        ___qtablewidgetitem8 = self.tabla.item(0, 1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Padilla", None));
        ___qtablewidgetitem9 = self.tabla.item(0, 2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"11111", None));
        ___qtablewidgetitem10 = self.tabla.item(0, 3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Av 123", None));
        ___qtablewidgetitem11 = self.tabla.item(0, 4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"123456", None));
        ___qtablewidgetitem12 = self.tabla.item(0, 5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"No tiene", None));
        self.tabla.setSortingEnabled(__sortingEnabled)

        self.lblNombre.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.lblDni.setText(QCoreApplication.translate("MainWindow", u"DNI", None))
        self.lblApellido.setText(QCoreApplication.translate("MainWindow", u"Apellido", None))
        self.lblDireccion.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n", None))
        self.lblTel.setText(QCoreApplication.translate("MainWindow", u"Tel\u00e9fono", None))
        self.lblFoto.setText(QCoreApplication.translate("MainWindow", u"Foto", None))
        self.btnAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir base de datos", None))
    # retranslateUi
