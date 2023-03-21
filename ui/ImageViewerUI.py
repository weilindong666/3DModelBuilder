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
    def __init__(self, addresses):
        super(ImageViewerUI, self).__init__()
        self.setupUi(self)
        self.addresses = addresses
        self.initCapacity()
        self.horizontalSlider.valueChanged.connect(self.sliderMove)
        self.spinBox.valueChanged.connect(self.spinBoxChange)

    def initCapacity(self):
        self.horizontalSlider.setMaximum(len(self.addresses) - 1)
        self.spinBox.setMaximum(len(self.addresses) - 1)

    def sliderMove(self):
        # 更改数字框（spinBox）数字
        self.spinBox.setValue(self.horizontalSlider.value())
        # 更换原始图像
        self.widget.updateA(self.addresses[self.horizontalSlider.value()], if_RGB=True)

    def spinBoxChange(self):
        self.horizontalSlider.setValue(self.spinBox.value())
        # 更换原始图像
        self.widget.updateA(self.addresses[self.spinBox.value()], if_RGB=True)

