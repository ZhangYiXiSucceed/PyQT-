# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Demo.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 619)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tbnOpen = QtWidgets.QPushButton(self.centralwidget)
        self.tbnOpen.setGeometry(QtCore.QRect(360, 20, 101, 31))
        self.tbnOpen.setObjectName("tbnOpen")
        self.tbnClose = QtWidgets.QPushButton(self.centralwidget)
        self.tbnClose.setGeometry(QtCore.QRect(640, 20, 121, 41))
        self.tbnClose.setObjectName("tbnClose")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(20, 160, 71, 41))
        self.label_1.setObjectName("label_1")
        self.cBPortName = QtWidgets.QComboBox(self.centralwidget)
        self.cBPortName.setGeometry(QtCore.QRect(110, 20, 191, 31))
        self.cBPortName.setObjectName("cBPortName")
        self.tEReceiveData = QtWidgets.QTextEdit(self.centralwidget)
        self.tEReceiveData.setGeometry(QtCore.QRect(20, 190, 761, 291))
        self.tEReceiveData.setObjectName("tEReceiveData")
        self.lESend = QtWidgets.QLineEdit(self.centralwidget)
        self.lESend.setGeometry(QtCore.QRect(20, 510, 631, 31))
        self.lESend.setObjectName("lESend")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 480, 71, 41))
        self.label_2.setObjectName("label_2")
        self.tbnSend = QtWidgets.QToolButton(self.centralwidget)
        self.tbnSend.setGeometry(QtCore.QRect(670, 510, 111, 31))
        self.tbnSend.setObjectName("tbnSend")
        self.tbnClear = QtWidgets.QToolButton(self.centralwidget)
        self.tbnClear.setGeometry(QtCore.QRect(670, 70, 111, 31))
        self.tbnClear.setObjectName("tbnClear")
        self.pBSelect = QtWidgets.QPushButton(self.centralwidget)
        self.pBSelect.setGeometry(QtCore.QRect(540, 70, 101, 31))
        self.pBSelect.setObjectName("pBSelect")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 20, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 101, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 101, 51))
        self.label_4.setObjectName("label_4")
        self.lEServerIP = QtWidgets.QLineEdit(self.centralwidget)
        self.lEServerIP.setGeometry(QtCore.QRect(110, 70, 191, 31))
        self.lEServerIP.setObjectName("lEServerIP")
        self.lEServerPort = QtWidgets.QLineEdit(self.centralwidget)
        self.lEServerPort.setGeometry(QtCore.QRect(360, 70, 101, 31))
        self.lEServerPort.setObjectName("lEServerPort")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 60, 51, 51))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tbnOpen.setText(_translate("MainWindow", "????????????"))
        self.tbnClose.setText(_translate("MainWindow", "????????????"))
        self.label_1.setText(_translate("MainWindow", "????????????"))
        self.label_2.setText(_translate("MainWindow", "????????????"))
        self.tbnSend.setText(_translate("MainWindow", "??????"))
        self.tbnClear.setText(_translate("MainWindow", "????????????"))
        self.pBSelect.setText(_translate("MainWindow", "????????????"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_3.setText(_translate("MainWindow", "??????IP?????????"))
        self.label_4.setText(_translate("MainWindow", "??????IP?????????"))
        self.label_5.setText(_translate("MainWindow", "?????????"))
