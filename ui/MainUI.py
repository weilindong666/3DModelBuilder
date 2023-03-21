# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/20 10:50
@Author  : 魏林栋
@Site    : 
@File    : MainUI.py
@Software: PyCharm
'''
from ui.ui.ui_MainUI import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QSplitter
from PySide2.QtCore import QSize, Qt, QPoint
from MySignals import MySignals
from ui.ui.list_widget import ListWidgetItem
import cv2
from threading import Thread


class MainUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        self.setupUi(self)
        self.MySignals = MySignals()
        # 由 vertical line 控制控件大小
        self.line.setMouseTracking(True)
        self.line_splitter = False
        self.line_move = 0
        self.line.mousePressEvent = self.mousePressEvent_line
        self.line.mouseMoveEvent = self.mouseMoveEvent_line
        self.line.mouseReleaseEvent = self.mouseReleaseEvent_line
        self.listWidget_1.resizeEvent = self.resizeEvent_listwidget

        self.action_import_dataset.triggered.connect(self.import_dataset)

    # def printnum(self):
    #     self.MySignals.my_first_signal.emit(5)

    def import_dataset(self):
        image = cv2.imread('./texture/1.png')
        height, width, channels = image.shape
        aspect_ratio = height/width
        item = ListWidgetItem(['./texture/1.png', './texture/none.png'], aspect_ratio)
        self.listWidget_1.addItem(item)
        self.listWidget_1.setItemWidget(item, item.image_widget)
        item.setSizeHint(QSize(self.listWidget_1.width(), aspect_ratio*self.listWidget_1.width()))

    def mousePressEvent_line(self, event):
        if event.button() == Qt.LeftButton:
            self.line_splitter = True

    def mouseMoveEvent_line(self, event):
        if self.line_splitter:
            move = event.pos().x() - self.line_move
            self.line_move = event.pos().x()
            if move < 0:
                if self.listWidget_1.width() > 50:
                    self.listWidget_1.resize(QSize(self.listWidget_1.width() + move, self.listWidget_1.height()))
                    self.line.move(self.line.pos().x() + move, self.line.pos().y())
                    self.widget.resize(QSize(self.widget.width() - move, self.widget.height()))
                    self.widget.move(self.widget.pos().x() + move, self.widget.pos().y())
            else:
                if self.widget.width() > 50:
                    self.listWidget_1.resize(QSize(self.listWidget_1.width() + move, self.listWidget_1.height()))
                    self.line.move(self.line.pos().x() + move, self.line.pos().y())
                    self.widget.resize(QSize(self.widget.width() - move, self.widget.height()))
                    self.widget.move(self.widget.pos().x() + move, self.widget.pos().y())


    def mouseReleaseEvent_line(self, event):
        if event.button() == Qt.LeftButton:
            self.line_splitter = False
            self.line_move = 0

    def resizeEvent_listwidget(self, event):
        if self.listWidget_1.count() > 0:
            for index in range(self.listWidget_1.count()):
                item = self.listWidget_1.item(index)
                if item is not None:
                    item.setSizeHint(QSize(int(self.listWidget_1.width()*0.95), int(item.aspect_ratio*self.listWidget_1.width())))