# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/21 11:08
@Author  : 魏林栋
@Site    : 
@File    : list_widget.py
@Software: PyCharm
'''
from PySide2.QtWidgets import QListWidgetItem, QMenu, QAction, QListWidget
from PySide2.QtCore import Qt
from ui.ui.Image_widget import ImageWidget
from ui.ImageViewerUI import ImageViewerUI


class ListWidget(QListWidget):
    def __init__(self, parent=None):
        super(ListWidget, self).__init__()
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.customMenue)

    def customMenue(self, pos):
        item = self.itemAt(pos)
        if item is not None:
            item.showMenue(pos)

class ListWidgetItem(QListWidgetItem):
    def __init__(self, address, aspect_ratio, parent=None, MySignals=None):
        super(ListWidgetItem, self).__init__()
        self.image_widget = None
        self.MySignals = MySignals
        self.aspect_ratio = aspect_ratio
        self.parent = parent
        if len(address) >= 2:
            self.addItems(address)
        else:
            self.addItem(address)
        self.actions = {'createModel': QAction('生成模型', parent), 'manualROI': QAction('手动勾画ROI', parent), 'autoROI': QAction('自动勾画ROI', parent)}

    def addItem(self, address):
        self.image_widget = ImageWidget()
        self.image_widget.updateA(address[0])
        self.image_widget.mouseDoubleClickEvent = self.mouseDoubleClickEvent_item

    def addItems(self, addresses):
        self.image_widget = ImageViewerUI(addresses)
        self.image_widget.widget.updateA(addresses[0])
        self.image_widget.widget.mouseDoubleClickEvent = self.mouseDoubleClickEvent_item

    def showMenue(self, pos):
        menue = QMenu()
        for act in self.actions.values():
            menue.addAction(act)
        action = menue.exec_(self.listWidget().mapToGlobal(pos))
        if action == self.actions['createModel']:
            self.MySignals.create_model_signal.emit('createModel')
        elif action == self.actions['manualROI']:
            self.MySignals.manual_ROI_signal.emit('manualROI')
        elif action == self.actions['autoROI']:
            self.MySignals.auto_ROI_signal.emit('autoROI')

    def mouseDoubleClickEvent_item(self, event):
        # 打开新界面进行ROI勾画
        print('double clicked')
        self.MySignals.manual_ROI_signal.emit('manualROI')