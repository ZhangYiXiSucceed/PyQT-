from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import PyQt5.QtWidgets as qw

from time import ctime
from Demo import Ui_MainWindow
import socket

import  os
import sys
import threading
import time




class Ui_Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Demo, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.tbnOpen.clicked.connect(self.OpenPort)
        self._ui.tbnSend.clicked.connect(self.Slot_tbnSend)
        self.lESendData = ''
        self._ui.tbnClose.clicked.connect(self.Slot_CloseSocket)

        self.over_threading = False


        self.hostname = socket.gethostname()
        self.self_ip_address = socket.getaddrinfo(self.hostname, None, socket.AF_INET)
        for add in self.self_ip_address:
            self._ui.cBPortName.addItem(add[4][0])
            print(add[4][0])


    # def SendData(self):
    #     while True:
    #         if self.lESendData != '':
    #             self.tcpCliSock.send(self.lESendData)  # 发送消息
    #             self.lESendData = ''

    def OpenPort(self):
        self.ServerIP = self._ui.lEServerIP.text()
        self.ServerPort = self._ui.lEServerPort.text()
        if self.ServerIP == '':
            qw.QMessageBox.critical(self, "错误", "IP 不能为空！", qw.QMessageBox.Abort)
            return
        if self.ServerPort == '':
            qw.QMessageBox.critical(self, "错误", "端口 不能为空！", qw.QMessageBox.Abort)
            return
        self.ServerIP = self._ui.lEServerIP.text()
        self.ServerPort = int(self._ui.lEServerPort.text(), 10)

        print(self.ServerIP)
        print(self.ServerPort)


        self.ADDR = (self.ServerIP, self.ServerPort)
        self.tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建socket对象
        self.tcpCliSock.connect(self.ADDR)  # 连接服务器

        self.ClientSendData = threading.Thread(target=self.Slot_Receive, args=())
        self.ClientSendData.start()
        self.over_threading = False
    def Slot_tbnSend(self):

        self.lESendData = self._ui.lESend.text()
        self.tcpCliSock.send(self.lESendData.encode('utf-8'))
        return

    def Slot_Receive(self):
        self.BUFSIZE = 1024
        while True:
            self._ui.tEReceiveData.append(self.tcpCliSock.recv(self.BUFSIZE).decode('utf-8'))
            if self.over_threading == True:
                break
        self.tcpCliSock.close()  # 关闭客户端
        return

    def Slot_CloseSocket(self):

        self.over_threading = True
        ## time.sleep(5)
        ## self.ClientSendData.join()
        ## self.tcpCliSock.close()  # 关闭客户端



        return
    def ClosePort(self):
        return


    def SendData(self):
        return

    def RecieveData(self):
        return




if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = Ui_Demo()
    MainWindow.show()
    sys.exit(app.exec_())