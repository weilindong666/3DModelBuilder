# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/24 13:49
@Author  : 魏林栋
@Site    : 
@File    : MDI_subWindows.py
@Software: PyCharm
'''
from PySide2.QtWidgets import QMdiSubWindow
from ui.ui.ui_OpenGLUI import Ui_OpenGL_Form
from ui.ui.ui_ImageShowUI import Ui_ImageShow_Form

class OpenGLUI(QMdiSubWindow, Ui_OpenGL_Form):
    def __init__(self, parent=None):
        super(OpenGLUI, self).__init__()
        self.setupUi(self)


class ImageShowUI(QMdiSubWindow, Ui_ImageShow_Form):
    def __init__(self, parent=None):
        super(ImageShowUI, self).__init__()
        self.setupUi(self)