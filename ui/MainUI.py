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
from PySide2.QtCore import QSize
from MySignals import MySignals
from ui.ui.list_widget import ListWidgetItem
import cv2

class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)
        self.MySignals = MySignals()
        self.action_import_dataset.triggered.connect(self.import_dataset)

    def printnum(self):
        self.MySignals.my_first_signal.emit(5)

    def import_dataset(self):
        image = cv2.imread('./texture/1.png')
        height, width, channels = image.shape
        aspect_ratio = height/width
        item = ListWidgetItem(['./texture/1.png', './texture/none.png'], self.listWidget_1)
        item.setSizeHint(QSize(self.listWidget_1.width(), aspect_ratio*self.listWidget_1.width()))
        # self.listWidget_1.addItem(item)