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
import cv2


class ListWidgetItem(QListWidgetItem):
    def __init__(self, address, aspect_ratio):
        super(ListWidgetItem, self).__init__()
        self.image_widget = None
        self.aspect_ratio = aspect_ratio
        if len(address) >= 2:
            self.addItems(address)
        else:
            self.addItem(address)


    def addItem(self, address):
        self.image_widget = ImageWidget()
        self.image_widget.updateA(address[0])

    def addItems(self, addresses):
        self.image_widget = ImageViewerUI(addresses)
        self.image_widget.widget.updateA(addresses[0])