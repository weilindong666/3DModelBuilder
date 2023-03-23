# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/20 11:17
@Author  : 魏林栋
@Site    : 
@File    : MySignals.py
@Software: PyCharm
'''
from PySide2.QtCore import Signal, QObject

class MySignals(QObject):
    my_first_signal = Signal(int)
    open_GL_window = Signal()
    create_model_signal = Signal()
    manual_ROI_signal = Signal()
    auto_ROI_signal = Signal()
    pass