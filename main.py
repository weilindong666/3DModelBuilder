# -*- coding: UTF-8 -*-
'''
@Time    : 2023/2/23 10:50
@Author  : 魏林栋
@Site    : 
@File    : main.py
@Software: PyCharm
'''
from PySide2.QtWidgets import QApplication
from MySignals import MySignals
from UI_Master import UI_Master

class MainService:
    def __init__(self):
        self.app = QApplication()
        self.UI_Master = UI_Master()
        self.MySignals = MySignals()
        self.initUI()
        self.initSignal()
        self.app.exec_()
        pass

    def initUI(self):

        self.UI_Master.MainUI.show()

    def initSignal(self):
        self.MySignals.my_first_signal.connect(self.firstSiganl)

    def firstSiganl(self, num):
        print(num)
        # self.app.exec_()


if __name__ == '__main__':
    MainService()

