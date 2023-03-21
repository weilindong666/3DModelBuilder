# -*- coding: UTF-8 -*-
'''
@Time    : 2023/2/24 14:12
@Author  : 魏林栋
@Site    : 
@File    : new.py
@Software: PyCharm
'''
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建两个 widget
        left_widget = QWidget(self)
        right_widget = QWidget(self)

        # 创建垂直线
        vline = QFrame(self)
        vline.setFrameShape(QFrame.VLine)
        vline.setFrameShadow(QFrame.Sunken)

        # 创建水平布局并将 widget 和垂直线添加到布局中
        hbox = QHBoxLayout()
        hbox.addWidget(left_widget)
        hbox.addWidget(vline)
        hbox.addWidget(right_widget)

        # 设置 widget 的最小大小
        left_widget.setMinimumSize(100, 100)
        right_widget.setMinimumSize(100, 100)

        # 创建 central widget 并将水平布局设置为其布局
        central_widget = QWidget(self)
        central_widget.setLayout(hbox)
        self.setCentralWidget(central_widget)

        # 设置垂直线的拖动事件
        vline.mousePressEvent = self.mousePressEvent1
        vline.mouseMoveEvent = self.mouseMoveEvent1
        vline.mouseReleaseEvent = self.mouseReleaseEvent1

        self.show()

    # 处理垂直线的拖动事件
    def mousePressEvent1(self, event):
        print('888')
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent1(self, event):
        print('666')
        if event.buttons() == Qt.LeftButton:
            delta = event.pos() - self.drag_start_position
            self.centralWidget().layout().setStretch(0, self.width() + delta.x())
            self.centralWidget().layout().setStretch(2, self.width() - delta.x())

    def mouseReleaseEvent1(self, event):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
