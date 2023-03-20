# -*- coding: UTF-8 -*-
'''
@Time    : 2023/2/24 15:36
@Author  : 魏林栋
@Site    : 
@File    : opengl_widget.py
@Software: PyCharm
'''
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from PySide2.QtWidgets import QOpenGLWidget

class openGL_Widget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)


    def mouseMoveEvent(self, event):
        print(event)
        # 这个三个是虚函数, 需要重写
        # paintGL
        # initializeGL
        # resizeGL

    # 启动时会先调用 initializeGL, 再调用 resizeGL , 最后调用两次 paintGL
    # 出现窗口覆盖等情况时, 会自动调用 paintGL
    # 调用过程参考 https://segmentfault.com/a/1190000002403921
    # 绘图之前的设置
    def initializeGL(self):
        glClearColor(0.2, 0.2, 0.2, 1)
        glEnable(GL_DEPTH_TEST)  # 开启深度测试
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)


        # 清除屏幕 深度缓存
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # 设置投影
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        k = 400 / 400
        glFrustum(-0.5 * k, 0.5 * k, -0.5, 0.5, 1.0, 20.0)  # 透视投影

        # 设置缩放
        glScale(1.0, 1.0, 1.0)

        # 设置视点
        gluLookAt(
            0.9, 1.9, 0.9,
            0.0, 0.0, 0.0,
            0.0, 1.0, 0.0
        )

        # 设置视口
        glViewport(0, 0, 400, 400)

    # 绘图函数
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glBegin(GL_LINES)  # 开始绘制
        # x轴
        glColor4f(1.0, 0.0, 0.0, 1.0)  # 红色不透明
        glVertex3f(-0.5, 0.0, 0.0)  # 设置x轴起始点 +
        glVertex3f(0.5, 0.0, 0.0)  # 设置x轴结束点  -

        # y轴
        glColor4f(0.0, 1.0, 0.0, 1.0)  # 绿色不透明
        glVertex3f(0.0, -0.5, 0.0)  # 设置x轴起始点 +
        glVertex3f(0.0, 0.5, 0.0)  # 设置x轴结束点  -

        # z轴
        glColor4f(0.0, 0.0, 1.0, 1.0)  # 蓝色不透明
        glVertex3f(0.0, 0.0, -0.5)  # 设置x轴起始点 +
        glVertex3f(0.0, 0.0, 0.5)  # 设置x轴结束点  -

        glEnd()  # 结束绘制


    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        # glLoadIdentity()
        # gluPerspective(45, w / h, 0.01, 100.0)
        # glMatrixMode(GL_MODELVIEW)
        # glLoadIdentity()
    #     gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

    def mousemotion(self, x, y):
        print(x, y)


import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class MyFigureCanvas(FigureCanvas):
    '''
    通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplotlib的关键
    '''

    def __init__(self, parent=None, width=10, height=5, xlim=(0, 10), ylim=(-2, 2), dpi=100):
        # 创建一个Figure
        fig = plt.Figure(figsize=(width, height), dpi=dpi, tight_layout=True)  # tight_layout: 用于去除画图时两边的空白

        FigureCanvas.__init__(self, fig)  # 初始化父类
        self.setParent(parent)
        self.axes = fig.add_subplot(111)  # 添加子图
        self.axes.spines['top'].set_visible(False)  # 去掉绘图时上面的横线
        self.axes.spines['right'].set_visible(False)  # 去掉绘图时右面的横线
        self.axes.set_xlim(xlim)
        self.axes.set_ylim(ylim)
        self.A = 1

    def updateA(self, x, y):
        self.axes.clear()
        self.axes.plot(x, y)
        self.axes.set_title('cos()')
        self.draw()