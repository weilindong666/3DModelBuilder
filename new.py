# -*- coding: UTF-8 -*-
'''
@Time    : 2023/2/24 14:12
@Author  : 魏林栋
@Site    : 
@File    : new.py
@Software: PyCharm
'''
from PySide2.QtWidgets import QApplication, QMainWindow, QOpenGLWidget
from ui.ui_MainWindow import Ui_MainWindow
import numpy as np

class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent=parent)
        # QMainWindow.__init__(self)
        # QOpenGLWidget.__init__(self)
        # self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.pushButton_display_click)
        # self.initializeGL()

    def pushButton_display_click(self):
        # self.ui.openGLWidget.update()	# 刷新图像
        # self.widget.show()
        x = np.arange(0, 2 * np.pi, np.pi / 100)
        y = np.cos(x)
        self.widget.updateA(x, y)


if __name__ == '__main__':
    app = QApplication()
    obj = MainWin()
    obj.show()
    app.exec_()