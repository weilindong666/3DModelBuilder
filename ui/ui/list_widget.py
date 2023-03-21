# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/21 11:08
@Author  : 魏林栋
@Site    : 
@File    : list_widget.py
@Software: PyCharm
'''
from PySide2.QtWidgets import QListWidgetItem
from ui.ui.Image_widget import ImageWidget
from ui.ImageViewerUI import ImageViewerUI
from threading import Thread
import time


class ListWidgetItem(QListWidgetItem):
    def __init__(self, address, list_widget):
        super(ListWidgetItem, self).__init__()
        self.image_widget = None
        self.list_widget = list_widget
        if len(address) >= 2:
            self.addItems(address)
        else:
            self.addItem(address)


    def addItem(self, address):
        self.image_widget = ImageWidget()
        self.image_widget.updateA(address[0])
        self.list_widget.addItem(self)
        self.list_widget.setItemWidget(self, self.image_widget)

    def addItems(self, addresses):
        self.image_widget = ImageViewerUI(addresses)
        self.image_widget.widget.updateA(addresses[0])
        self.list_widget.addItem(self)
        self.list_widget.setItemWidget(self, self.image_widget)