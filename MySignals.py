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
    create_model_signal = Signal(dict)
    manual_ROI_signal = Signal(dict)
    auto_ROI_signal = Signal(dict)
    clear_listwidget_signal = Signal()
    listwidget_item_add_finished_signal = Signal()
    open_manual_ROI_UI = Signal(dict)
    show_image_on_MDI = Signal(dict)
    pass