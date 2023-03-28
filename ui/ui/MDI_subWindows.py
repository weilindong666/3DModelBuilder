# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/24 13:49
@Author  : 魏林栋
@Site    : 
@File    : MDI_subWindows.py
@Software: PyCharm
'''
from PySide2.QtWidgets import QMdiSubWindow, QVBoxLayout, QMdiArea
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt
from ui.ui.opengl_widget import openGL_Widget
from ui.ui.Image_widget import MyImageWidget

class MyMdiWidget(QMdiArea):
    def __init__(self, parent=None):
        super(MyMdiWidget, self).__init__()
        self.MySignals = None
        self.MDI_sub_windows = {'createModel': OpenGLUI, 'manualROI': ImageShowUI, 'autoROI': ImageShowUI}

    def openMDIUI(self, kwargs):
        UI_name = kwargs['UI_name']
        subWindow = self.MDI_sub_windows[UI_name](**kwargs)
        self.addSubWindow(subWindow)
        subWindow.showMaximized()

    def loadSignals(self, MySignals):
        self.MySignals = MySignals
        self.MySignals.open_manual_ROI_UI.connect(self.openMDIUI)
        self.MySignals.create_model_signal.connect(self.openMDIUI)

class OpenGLUI(QMdiSubWindow):
    def __init__(self, **kwargs):
        super().__init__()
        self.setWindowTitle("Create Model")
        self.setGeometry(200, 200, 400, 300)
        self.widget = openGL_Widget(self)
        self.setWindowIcon(QIcon(''))
        self.layout = QVBoxLayout(self.widget)
        self.setWidget(self.widget)


class ImageShowUI(QMdiSubWindow):
    def __init__(self, **kwargs):
        super(ImageShowUI, self).__init__()
        self.initUI()
        self.importAttribute(**kwargs)
        self.MySignals.show_image_on_MDI.connect(self.showImage)
        self.draw = False

    def initUI(self):
        self.setWindowTitle("Image Show")
        self.setGeometry(200, 200, 400, 300)
        self.widget = MyImageWidget()
        self.widget.mousePressEvent = self.mousePressEvent_image
        self.widget.mouseMoveEvent = self.mouseMoveEvent_image
        self.widget.mouseReleaseEvent = self.mouseReleaseEvent_image
        self.setWindowIcon(QIcon(''))
        self.layout = QVBoxLayout(self.widget)
        self.setWidget(self.widget)

    def importAttribute(self, **kwargs):
        self.MySignals = kwargs['MySignals']
        self.Pool = kwargs['Pool']
        self.aspect_ratio = kwargs['aspectRatio']
        self.parent = kwargs['parent']
        self.images = kwargs['images']
        self.showImage(kwargs)
        self.repaint()

    def showImage(self, kwargs):
        image = kwargs['images']
        self.widget.updateA(image, aspect='equal')

    def mousePressEvent_image(self, event):
        if event.button() == Qt.LeftButton:
            self.draw = True

    def mouseMoveEvent_image(self, event):
        if event.button() == Qt.LeftButton and self.draw:
            pass

    def mouseReleaseEvent_image(self, event):
        if event.button() == Qt.LeftButton:
            self.draw = False