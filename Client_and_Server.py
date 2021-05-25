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


socket.setdefaulttimeout(5)


class Ui_Demo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Demo, self).__init__()
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.tbnOpen.clicked.connect(self.OpenPort)
        self._ui.tbnSend.clicked.connect(self.Slot_tbnSend)
        self._ui.tbnClear.clicked.connect(self.ClearShow)
        self.lESendData = ''
        self._ui.tbnClose.clicked.connect(self.Slot_CloseSocket)

        self.over_threading = False
        self.IsOpen = False


        self.hostname = socket.gethostname()
        self.self_ip_address = socket.getaddrinfo(self.hostname, None, socket.AF_INET)
        for add in self.self_ip_address:
            self._ui.cBPortName.addItem(add[4][0])
            print(add[4][0])
        self._ui.tbnClose.setDisabled(True)

        self._ui.lEServerPort.setText('51230')
        self._ui.lEServerIP.setText('169.254.100.10')


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
        self.tcpCliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)  # 创建socket对象

        self.tcpCliSock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)

        self.tcpCliSock.connect(self.ADDR)  # 连接服务器

        try:
            self.ClientSendData = threading.Thread(target=self.Slot_Receive)
        except Exception as e:
            print(e)
        self.ClientSendData.start()
        print('start %s' % self.ClientSendData.name)
        print('当前活着的线程列表为:', threading.enumerate())

        print('当前处于活动的线程个数为{} ,当前主线程为{},当前线程ID为{}'.format(threading.active_count(), threading.main_thread(),
                                                          threading.get_ident()))
        self.over_threading = False
        self._ui.tbnOpen.setDisabled(True)
        self._ui.tbnClose.setDisabled(False)
        # self.tcpCliSock.settimeout(5)

        self.IsOpen = True

    def Slot_tbnSend(self):

        if self.IsOpen == True:
            self.lESendData = self._ui.lESend.text()
            self.tcpCliSock.send(self.lESendData.encode('utf-8'))
            return

    def Slot_Receive(self):
        self.BUFSIZE = 1024
        while self.over_threading == False:
            try:
                rx = self.tcpCliSock.recv(self.BUFSIZE).decode('utf-8')
            except socket.timeout:
                continue
            # except TimeoutError:
            #     continue
            # except ConnectionError:
            #     self.over_threading = True
            #     break
            self._ui.tEReceiveData.append(rx)


        return

    def Slot_CloseSocket(self):

        self.IsOpen = False
        self.over_threading = True
        self.ClientSendData.join()
        self.tcpCliSock.close()  # 关闭客户端
        self._ui.tbnOpen.setDisabled(False)
        ## time.sleep(5)

        ## self.tcpCliSock.close()  # 关闭客户端



        return
    def ClearShow(self):
        self._ui.tEReceiveData.setText('')
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