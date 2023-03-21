# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/20 10:50
@Author  : 魏林栋
@Site    : 
@File    : MainUI.py
@Software: PyCharm
'''
from ui.ui.ui_MainUI import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow
from MySignals import MySignals
from ui.ui.list_widget import ListWidgetItem

class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)
        self.MySignals = MySignals()
        self.action_import_dataset.triggered.connect(self.import_dataset)

    def printnum(self):
        self.MySignals.my_first_signal.emit(5)

    def import_dataset(self):
        item = ListWidgetItem(['./texture/none.png'])
        self.listWidget_1.addItem(item)