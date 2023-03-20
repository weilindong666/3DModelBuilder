# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/20 10:50
@Author  : 魏林栋
@Site    : 
@File    : MainUI.py
@Software: PyCharm
'''
from ui.ui.ui_MainUI import Ui_MainWindow
from PySide2.QtWidgets import QApplication, QMainWindow
from MySignals import MySignals

class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)
        self.MySignals = MySignals()
        self.pushButton.clicked.connect(self.printnum)

    def printnum(self):
        self.MySignals.my_first_signal.emit(5)
        print('666')