# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/21 13:36
@Author  : 魏林栋
@Site    : 
@File    : ImageViewerUI.py
@Software: PyCharm
'''
from ui.ui.ui_ImageViewerUI import Ui_Form
from PySide2.QtWidgets import QWidget

class ImageViewerUI(QWidget, Ui_Form):
    def __init__(self):
        super(ImageViewerUI, self).__init__()
        self.setupUi(self)

