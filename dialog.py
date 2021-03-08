# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import PyQt5.QtWidgets as qw
import sys
import SeednKey
import os
import AllGlogol

class Ui_Dialog(QWidget):
    def __init__(self):
        super(Ui_Dialog, self).__init__()

        self.buttonBox = QtWidgets.QDialogButtonBox()
        self.buttonBox.setGeometry(QtCore.QRect(240, 470, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.cwd = os.getcwd()

        self.SeedKeyAddr = QLineEdit()
        self.SelectAddr = QPushButton()
        self.SelectAddr.setText('...')
        self.SeedKeyAddr.setFixedHeight(30)
        self.SeedKeyAddr.setFixedWidth(280)
        self.SelectAddr.setFixedWidth(60)
        self.SelectAddr.setFixedHeight(30)
        self.SeedKeyAddr.setPlaceholderText('E:/WorkSpace/BT/DemoProject/SeednKey.dll')
        self.SelectAddr.clicked.connect(self.Slot_SelectAddr)



        self.Seed = QLineEdit()
        self.DescriptionSeed = QLabel()
        self.Key = QLineEdit()
        self.DescriptionKey = QLabel()
        self.DescriptionSeed.setText('Seed')
        self.DescriptionKey.setText('Key')
        self.Seed.setFixedWidth(200)
        self.Seed.setFixedHeight(25)
        self.Key.setFixedHeight(25)
        self.Key.setFixedWidth(200)
        self.Seed.setPlaceholderText('例如：0D 4A 1F FE')

        self.Level = QComboBox()
        self.Level.setFixedWidth(130)
        self.Level.setFixedHeight(30)
        self.DescriptionLevel = QLabel()
        self.DescriptionLevel.setText('Level')
        self.Level.activated.connect(self.Slot_LevelFunction)

        self.Level.addItem('0x01')
        self.Level.addItem('0x05')

        self.Mask = QComboBox()
        self.Mask.setFixedWidth(130)
        self.Mask.setFixedHeight(30)
        self.DescriptionMask = QLabel()
        self.DescriptionMask.setText('Mask')
        self.Mask.setDisabled(True)

        self.Mask.addItem('0xC583C583')
        self.Mask.addItem('0xF583F583')

        self.Btn_Start = QPushButton()
        self.Btn_Cancel = QPushButton()
        self.Btn_Start.setText('Start')
        self.Btn_Cancel.setText('Cancel')
        self.Btn_Start.setFixedSize(75,35)
        self.Btn_Cancel.setFixedSize(75,35)
        self.Btn_Start.setDisabled(False)
        self.Btn_Cancel.setDisabled(False)
        self.Btn_Start.clicked.connect(self.Slot_SeedKeyCalculate)
        self.Btn_Cancel.clicked.connect(self.Slot_CancleFunction)

        self.Group_Console = QGroupBox()
        self.Group_Seedkey = QGroupBox()
        self.Group_Calculate = QGroupBox()

        self.Group_Console.setTitle('Console')
        self.Group_Seedkey.setTitle('Seedkey')
        self.Group_Calculate.setTitle('Calculate')

        self.Group_Console.setFixedHeight(100)
        self.Group_Console.setFixedWidth(400)

        self.Group_Seedkey.setFixedHeight(100)
        self.Group_Seedkey.setFixedWidth(400)

        self.Group_Calculate.setFixedHeight(200)
        self.Group_Calculate.setFixedWidth(400)

        self.h1_layout = QHBoxLayout()
        self.h1_layout.addWidget(self.DescriptionLevel)
        self.h1_layout.addWidget(self.Level)
        self.h1_layout.addWidget(self.DescriptionMask)
        self.h1_layout.addWidget(self.Mask)

        self.v_layout = QVBoxLayout()
        self.v1_layout = QVBoxLayout()
        self.v2_layout = QVBoxLayout()

        self.v2_h1_layout = QHBoxLayout()
        self.v2_h1_layout.addWidget(self.SeedKeyAddr)
        self.v2_h1_layout.addWidget(self.SelectAddr)
        self.v2_layout.addLayout(self.v2_h1_layout)

        self.v2_h2_layout = QHBoxLayout()
        self.v2_h2_layout.addWidget(self.Btn_Start)
        self.v2_h2_layout.addWidget(self.Btn_Cancel)
        self.v2_layout.addLayout(self.v2_h2_layout)


        self.v1_h1_layout = QHBoxLayout()
        self.v1_h2_layout = QHBoxLayout()

        self.v1_h1_layout.addWidget(self.DescriptionSeed)
        self.v1_h1_layout.addWidget(self.Seed)
        self.v1_h2_layout.addWidget(self.DescriptionKey)
        self.v1_h2_layout.addWidget(self.Key)

        self.v1_layout.addLayout(self.v1_h1_layout)
        self.v1_layout.addLayout(self.v1_h2_layout)

        self.Group_Console.setLayout(self.h1_layout)
        self.Group_Seedkey.setLayout(self.v1_layout)
        self.Group_Calculate.setLayout(self.v2_layout)

        self.v_layout.addWidget(self.Group_Console)
        self.v_layout.addWidget(self.Group_Seedkey)
        self.v_layout.addWidget(self.Group_Calculate)
        self.setLayout(self.v_layout)


    def Slot_LevelFunction(self):
        if self.Level.currentText() == '0x01':
            self.Mask.setCurrentIndex(0)
        if self.Level.currentText() == '0x05':
            self.Mask.setCurrentIndex(1)
        return

    def Slot_SeedKeyCalculate(self):
        if self.Seed.text() == '':
            qw.QMessageBox.critical(self, "错误", "seed 不能为空！", qw.QMessageBox.Abort | qw.QMessageBox.Cancel)
        else:
            seed = []
            key = []
            LevelNumber = int(self.Level.currentText(), 16)

            # seedNumber = int(self.Seed.text(),16)
            # LevelNumber = int(self.Level.currentText(),16)
            #
            # print(seedNumber)
            # print(LevelNumber)
            #
            # seed = bytearray([0x00,0x00,0x00,0x00])
            # seed[0] = int(seedNumber / 65536 / 256)
            # seed[1] = int(seedNumber / 65536 % 256)
            # seed[2] = int(seedNumber / 256 % 256)
            # seed[3] = int(seedNumber % 256)
            #
            # print(seed[0],seed[1],seed[2],seed[3])
            #
            # key = SeednKey.SeedToKeyFromDll(seed,LevelNumber)
            #
            # KeyNumber = key[0]*65536*256+key[1]*65536+key[2]*256+key[3]
            #
            # str = ''
            # str +='0x';
            # str +='%x' %KeyNumber
            # self.Key.setText(str)

            seed = self.Seed.text().split(' ')

            # print(seed)
            seedNumber = []
            seedNumber = bytearray([0x00, 0x00, 0x00, 0x00])

            seedNumber[0] = int(seed[0],16)
            seedNumber[1] = int(seed[1],16)
            seedNumber[2] = int(seed[2],16)
            seedNumber[3] = int(seed[3],16)

            key = SeednKey.SeedToKeyFromDll(seedNumber, LevelNumber)

            if key == None:
                return

            keyNumber = ['00','00','00','00']

            # print(keyNumber[0])

            keyNumber[0] = '%x' %key[0]
            keyNumber[1] = '%x' %key[1]
            keyNumber[2] = '%x' %key[2]
            keyNumber[3] = '%x' %key[3]

            Numstr = ''
            Numstr += keyNumber[0]
            Numstr += ' '
            Numstr += keyNumber[1]
            Numstr += ' '
            Numstr += keyNumber[2]
            Numstr += ' '
            Numstr += keyNumber[3]
            Numstr += ' '

            self.Key.setText(Numstr)

        return
    def Slot_CancleFunction(self):
        self.close()
        return
    def Slot_SelectAddr(self):
        fileName_choose, filetype = QFileDialog.getOpenFileName(self, '...', self.cwd, "Files (*.dll)")
        if fileName_choose == "":
            return
        self.SeedKeyAddr.setText(fileName_choose)
        AllGlogol.set_value('Addr',fileName_choose)
        return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    AllGlogol._init()
    mywindow = Ui_Dialog()
    mywindow.show()
    sys.exit(app.exec())
