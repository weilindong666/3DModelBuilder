# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/21 11:08
@Author  : 魏林栋
@Site    : 
@File    : list_widget.py
@Software: PyCharm
'''
from PySide2.QtWidgets import QListWidgetItem, QMenu, QAction
from ui.ui.Image_widget import ImageWidget
from ui.ImageViewerUI import ImageViewerUI


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

    def addItems(self, addresses):
        self.image_widget = ImageViewerUI(addresses)
        self.image_widget.widget.updateA(addresses[0])

    def showMenue(self, pos):
        menue = QMenu()
        for act in self.actions.values():
            menue.addAction(act)
        action = menue.exec_(self.listWidget().mapToGlobal(pos))
        if action == self.actions['createModel']:
            self.MySignals.create_model_signal.emit()
        elif action == self.actions['manualROI']:
            self.MySignals.manual_ROI_signal.emit()
        elif action == self.actions['autoROI']:
            self.MySignals.auto_ROI_signal.emit()

    # def process(self):
    #     self.MySigals.open_GL_window.emit()