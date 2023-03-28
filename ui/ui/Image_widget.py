# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/21 11:31
@Author  : 魏林栋
@Site    : 
@File    : Image_widget.py
@Software: PyCharm
'''
import cv2
import os
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
# import matplotlib.image as img

class MyImageWidget(FigureCanvas):
    def __init__(self, parent=None):
        fig = plt.figure(dpi=100, tight_layout=True, facecolor='black')
        fig.patch.set_alpha(0.0)
        FigureCanvas.__init__(self, fig)
        self.axes = fig.add_subplot(111)
        # self.axes.axis('off')
        self.axes.spines['top'].set_visible(False)  # 去掉绘图时上面的横线
        self.axes.spines['right'].set_visible(False)  # 去掉绘图时右面的横线
        self.axes.spines['left'].set_visible(False)  # 去掉绘图时左面的横线
        self.axes.spines['bottom'].set_visible(False)  # 去掉绘图时下面的横线
        self.axes.get_xaxis().set_visible(False)
        self.axes.get_yaxis().set_visible(False)
        # self.updateA('./result/feature_stats.png')
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
        self.axes.set_position([0, 0, 1, 1])

    def updateA(self, image, aspect='auto', if_RGB=False, title=None):
        self.axes.clear()
        if os.path.isfile(image):
            image = cv2.imread(image)
        if if_RGB:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        if title is not None:
            self.axes.set_title(title)
        self.axes.imshow(image, extent=(0, 1000, 0, 1000), aspect=aspect)
        self.draw()