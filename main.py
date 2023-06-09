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
from lib.Tools import Tools
from concurrent.futures import ThreadPoolExecutor

class MainService:
    def __init__(self):
        self.tools = Tools()
        self.Pool = ThreadPoolExecutor(max_workers=2)
        self.tools.clearFolder('./temp')
        self.MySignals = MySignals()
        self.app = QApplication()
        self.UI_Master = UI_Master(self.MySignals, self.Pool, self.tools)
        self.initUI()
        self.initSignal()
        self.app.aboutToQuit.connect(self.quit)


    def initUI(self):
        self.UI_Master.MainUI.show()

    def initSignal(self):
        self.MySignals.my_first_signal.connect(self.firstSiganl)

    def openImageShowUI(self):
        pass

    def createModel(self):
        print('create model')

    def firstSiganl(self, num):
        print(num)
        # self.app.exec_()
    def quit(self):
        self.tools.clearFolder('./temp')
        self.UI_Master.MainUI.close()
        self.Pool.shutdown(wait=False)

if __name__ == '__main__':
    app = MainService()
    app.app.exec_()
