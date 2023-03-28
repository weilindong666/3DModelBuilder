# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/21 11:08
@Author  : 魏林栋
@Site    : 
@File    : MyListWidget.py
@Software: PyCharm
'''
from PySide2.QtWidgets import QListWidgetItem, QMenu, QAction, QListWidget
from PySide2.QtCore import Qt, QSize
from ui.ui.Image_widget import MyImageWidget
from ui.ImageViewerUI import ImageViewerUI


class MyListWidget(QListWidget):
    MySignals = None
    Pool = None
    Tools = None
    items = []
    def __init__(self, parent=None):
        super(MyListWidget, self).__init__()
        self.data = {}
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.customMenue)

    def resizeEvent(self, event):
        if self.count() > 0:
            for index in range(self.count()):
                item = self.item(index)
                if item is not None:
                    self.Pool.submit(self.resizeThread, item, self.width())

    def resizeThread(self, item, width):
        item.setSizeHint(QSize(int(width * 0.95), int(item.aspect_ratio * width)))

    def customMenue(self, pos):
        item = self.itemAt(pos)
        if item is not None:
            item.showMenue(pos)

    def loadTools(self, MySignals, Pool, Tools):
        self.MySignals = MySignals
        self.MySignals.manual_ROI_signal.connect(self.openManualROIUI)
        self.MySignals.clear_listwidget_signal.connect(self.clearListWidget)
        self.Pool = Pool
        self.Tools = Tools
        self.item_model = {'parent': self, 'MySignals': self.MySignals, 'Pool': self.Pool, 'Tools': self.Tools, 'class': 'item'}

    def createItem(self, data):
        data.update(self.item_model)
        item = MyListWidgetItem(**data)
        self.addItem(item)
        self.setItemWidget(item, item.image_widget)
        item.setSizeHint(QSize(self.width(), data['aspectRatio'] * self.width()))
        # MySignals.manual_ROI_signal.emit('manualROI', {})

    def openManualROIUI(self, data):
        # 把所有图片显示在列表里
        images = data['images']
        items = []
        for image in images:
            data['images'] = [image]
            items.append(MyListWidgetItem(**data))
        for item in items:
            self.Pool.submit(self.addItemThread, item)
        self.repaint()
        self.MySignals.listwidget_item_add_finished_signal.emit()

    def addItemThread(self, item):
        self.addItem(item)
        self.setItemWidget(item, item.image_widget)
        item.setSizeHint(QSize(self.width(), item.aspect_ratio * self.width()))

    def clearListWidget(self):
        for index in range(self.count()):
            item = self.item(index)
            if item is not None:
                data = item.exportAttribute()
                self.items.append(data)
        self.clear()

    def back(self):
        self.clear()
        for data in self.items:
            self.createItem(data)
        self.items = []

# 列表item类
class MyListWidgetItem(QListWidgetItem):
    def __init__(self, **kwargs):
        super(MyListWidgetItem, self).__init__()
        self.image_widget = None
        self.importAttribute(**kwargs)
        self.finished = True
        if len(self.images) >= 2:
            self.addItems(self.images)
        else:
            self.addItem(self.images)
        self.actions = {'createModel': QAction('生成模型', self.parent), 'manualROI': QAction('手动勾画ROI', self.parent),
                        'autoROI': QAction('自动勾画ROI', self.parent)}
        self.MySignals.listwidget_item_add_finished_signal.connect(lambda : self.receivefinishedsignal)

    def addItem(self, address):
        self.image_widget = MyImageWidget()
        self.image_widget.updateA(address[0])
        self.image_widget.mousePressEvent = self.mousePressEvent_item

    def addItems(self, addresses):
        self.image_widget = ImageViewerUI(addresses)
        self.image_widget.widget.updateA(addresses[0])
        self.image_widget.widget.mouseDoubleClickEvent = self.mouseDoubleClickEvent_item

    def showMenue(self, pos):
        if self.class_ == 'item':
            menue = QMenu()
            for act in self.actions.values():
                menue.addAction(act)
            action = menue.exec_(self.listWidget().mapToGlobal(pos))
            if action == self.actions['createModel']:
                self.MySignals.create_model_signal.emit({'UI_name': 'createModel'})
            elif action == self.actions['manualROI']:
                self.openManualROIUI()
            elif action == self.actions['autoROI']:
                self.MySignals.auto_ROI_signal.emit({'UI_name': 'autoROI'})

    def mouseDoubleClickEvent_item(self, event):
        # 双击打开勾画ROI界面，列表清空把所有图像展示在列表里
        self.openManualROIUI()

    def openManualROIUI(self):
        data = self.exportAttribute(UI_name='manualROI')
        data['class'] = 'normal'
        self.MySignals.clear_listwidget_signal.emit()
        images = data['images']
        data['images'] = images[0]
        self.MySignals.open_manual_ROI_UI.emit(data)
        index_o = 0
        for index_n in range(3, len(images), 3):
            data['images'] = images[index_o: index_n]
            index_o = index_n
            self.MySignals.manual_ROI_signal.emit(data)
            self.finished = True
            for _ in range(200):
                if not self.finished:
                    break

    def openManualROIUIThread(self, data):
        self.MySignals.manual_ROI_signal.emit(data)

    def receivefinishedsignal(self):
        self.finished = False

    def exportAttribute(self, **kwargs):
        data = {'images': self.images, 'aspectRatio': self.aspect_ratio, 'parent': self.parent,
                'MySignals': self.MySignals, 'Pool': self.Pool, 'Tools': self.Tools}
        data.update(kwargs)
        return data

    def importAttribute(self, **kwargs):
        self.MySignals = kwargs['MySignals']
        self.Pool = kwargs['Pool']
        self.Tools = kwargs['Tools']
        self.aspect_ratio = kwargs['aspectRatio']
        self.parent = kwargs['parent']
        self.images = kwargs['images']
        self.class_ = kwargs['class']

    def mousePressEvent_item(self, event):
        if event.button() == Qt.LeftButton and self.class_ == 'normal':
            data = {'images': self.images[0], 'aspectRatio': self.aspect_ratio}
            self.MySignals.show_image_on_MDI.emit(data)