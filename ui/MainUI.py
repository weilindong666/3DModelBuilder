# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/20 10:50
@Author  : 魏林栋
@Site    : 
@File    : MainUI.py
@Software: PyCharm
'''
import os.path
from ui.ui.ui_MainUI import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow, QFileDialog
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QIcon
from UIC import UIC


class MainUI(QMainWindow, Ui_MainWindow, UIC):
    def __init__(self, MySignals, Pool, Tools):
        super(MainUI, self).__init__()
        self.setupUi(self)
        self.initIcon()
        self.MySignals = MySignals
        self.Pool = Pool
        self.tools = Tools
        self.widget.loadSignals(self.MySignals)
        self.listWidget.loadTools(self.MySignals, self.Pool, self.tools)
        # 由 vertical line 控制控件大小
        self.line.setMouseTracking(True)
        self.line_splitter = False
        self.line_move = 0
        self.line.mousePressEvent = self.mousePressEvent_line
        self.line.mouseMoveEvent = self.mouseMoveEvent_line
        self.line.mouseReleaseEvent = self.mouseReleaseEvent_line
        # 导入文件
        self.action_import_single_file.triggered.connect(self.importSingleFile)
        self.action_import_folder.triggered.connect(self.importFolder)
        # 返回原来的界面
        self.action_go_back.triggered.connect(self.listWidget.back)

    def initIcon(self):
        self.setWindowIcon(QIcon(self.app_icon))
        self.action_import_single_file.setIcon(QIcon(self.import_single_file_icon))
        self.action_import_folder.setIcon(QIcon(self.import_folder_icon))

    def importSingleFile(self):
        filepath, _ = QFileDialog.getOpenFileName(self, '选择单个文件', self.nowpath, '(*.nii.gz *.dcm)')
        images = []
        if filepath:
            if filepath.endswith('nii.gz'):
                images = self.tools.niigzToPng(filepath, self.nowpath + '/temp', self)
            elif filepath.endswith('dcm'):
                images = self.tools.dcmToPng(filepath, self.nowpath + '/temp/' + os.path.basename(filepath).split('.')[0], self)
        else:
            return
        aspect_ratio = self.tools.getAspectRatio(images[0])
        self.listWidget.createItem({'images': images, 'aspectRatio': aspect_ratio})

    def importFolder(self):
        '''还没写完, 还可以再改一改图像的显示'''
        filePath = QFileDialog.getExistingDirectory(self, "选择文件夹")
        if filePath:
            # 查找所有的dcm文件或者nii.gz文件
            dcms = self.tools.findAllParticularFiles(filePath)
            niis = self.tools.findAllParticularFiles(filePath, type_='nii.gz')
            # 把文件中的图像提取出来
            if dcms:
                image_dcm = []
                for dcm in dcms:
                    image = self.tools.dcmToPng(dcm, self.nowpath + './temp/' + os.path.basename(filePath))[0]
                    image_dcm.append(image)
                aspect_ratio = self.tools.getAspectRatio(image_dcm[0])
                self.listWidget.createItem({'images': image_dcm, 'aspectRatio': aspect_ratio})
            if niis:
                for nii in niis:
                    images = self.tools.niigzToPng(nii, self.nowpath + '/temp')
                    aspect_ratio = self.tools.getAspectRatio(images[0])
                    self.listWidget.createItem({'images': images, 'aspectRatio': aspect_ratio})

    def mousePressEvent_line(self, event):
        if event.button() == Qt.LeftButton:
            self.line_splitter = True

    def mouseMoveEvent_line(self, event):
        if self.line_splitter:
            move = event.pos().x() - self.line_move
            if abs(move) < 2:
                return
            self.line_move = event.pos().x()
            self.Pool.submit(self.resizeWidget, move)

    def mouseReleaseEvent_line(self, event):
        if event.button() == Qt.LeftButton:
            self.listWidget.repaint()
            self.line.repaint()
            self.widget.repaint()
            self.line_splitter = False
            self.line_move = 0

    def resizeWidget(self, move):
        if move < 0:
            if self.listWidget.width() > 50:
                width = self.listWidget.width()
                self.listWidget.resize(QSize(width + move, self.listWidget.height()))
                self.line.move(width + move + 15, self.line.pos().y())
                self.widget.resize(QSize(self.widget.width() - move, self.widget.height()))
                self.widget.move(width + move + 24, self.widget.pos().y())
        else:
            if self.widget.width() > 50:
                width = self.listWidget.width()
                self.listWidget.resize(QSize(width + move, self.listWidget.height()))
                self.line.move(width + move + 15, self.line.pos().y())
                self.widget.resize(QSize(self.widget.width() - move, self.widget.height()))
                self.widget.move(width + move + 24, self.widget.pos().y())

    def resizeEvent(self, event):
        pass
        # print(self.widget.width(), self.widget.height())