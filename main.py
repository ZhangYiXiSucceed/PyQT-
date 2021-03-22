import ctypes
import sys
from ctypes import *

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import  AllGlogol

from Demo import *
from dialog import *


Num = 0x01


class MainTabWindow(QTabWidget):
    def __init__(self, parent=None):
        super(MainTabWindow, self).__init__(parent)
        self.resize(1360,800)
        self.setWindowTitle('OTA_Console')
        self.setWindowIcon(QIcon('E:/WorkSpace/BT/tool/Download/OTA.jpg'))

        self.Tab_Demo = Ui_MainWindow()
        self.Tab_dialog = Ui_Dialog()


        self.addTab(self.Tab_Demo,'CAN')
        self.addTab(self.Tab_dialog,'ProcessSetting')



def LoadDll():
    # lib = ctypes.CDLL("E:\WorkSpace\BT\DemoProject\SeednKey.dll")
    # lib.HelloWorld()
    # lib.Sub.argtypes = (c_int,c_int)
    # lib.Sub.restype = c_int
    # print(lib.Sub(3,1))
    # return lib.Sub(3,1)
    dll = ctypes.CDLL("E:\WorkSpace\BT\DemoProject\SeednKey.dll")
    INPUT = c_ubyte * 4
    # 实例化一个长度为2的整型数组
    seed = INPUT()
    key = INPUT()
    # 为数组赋值（input这个数组是不支持迭代的）
    seed[0] = 0x4E
    seed[1] = 0x16
    seed[2] = 0xE1
    seed[3] = 0xD9

    dll.GenerateKeyEx(seed,0x05,key)
    print('%x' % key[0],'%x' %key[1],'%x' % key[2],'%x' % key[3])

if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = MainTabWindow()

    LoadDll()
    AllGlogol._init()

    # ui.tbnOpen.clicked.connect(OpenSuccess)
    # ui.tbnClose.clicked.connect(CloseSuccess)
    # ui.tbnSend.clicked.connect(SendSuccess)
    # ui.tbnClear.clicked.connect(ClearSuccess)
    # ui.pBSelect.clicked.connect(SelectSuccess)

    MainWindow.show()
    sys.exit(app.exec_())

