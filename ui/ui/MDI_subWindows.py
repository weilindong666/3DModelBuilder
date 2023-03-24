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
from ui.ui.opengl_widget import openGL_Widget

class MyMdiWidget(QMdiArea):
    def __init__(self, parent=None):
        super(MyMdiWidget, self).__init__()
        self.MySignals = None
        self.MDI_sub_windows = {'createModel': OpenGLUI, 'manualROI': ImageShowUI, 'autoROI': ImageShowUI}

    def openMDIUI(self, UI_name):
        subWindow = self.MDI_sub_windows[UI_name]()
        self.addSubWindow(subWindow)
        subWindow.showMaximized()

    def loadSignals(self, MySignals):
        self.MySignals = MySignals
        self.MySignals.manual_ROI_signal.connect(self.openMDIUI)
        self.MySignals.create_model_signal.connect(self.openMDIUI)

class OpenGLUI(QMdiSubWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Model")
        self.setGeometry(200, 200, 400, 300)
        self.widget = openGL_Widget(self)
        self.setWindowIcon(QIcon(''))
        self.layout = QVBoxLayout(self.widget)
        self.setWidget(self.widget)


class ImageShowUI(QMdiSubWindow):
    def __init__(self):
        super(ImageShowUI, self).__init__()
        self.setWindowTitle("Create Model")
        self.setGeometry(200, 200, 400, 300)
