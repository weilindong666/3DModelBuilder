# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/22 21:11
@Author  : 魏林栋
@Site    : 
@File    : UIC.py
@Software: PyCharm
'''
from PySide2.QtWidgets import QFileDialog, QMessageBox
import os

class UIC:
    nowpath = os.path.dirname(__file__).replace('\\', '/')
    image_none = nowpath + '/texture/none.png'
    def __init__(self):
        pass

    def worning(self, father, info):
        QMessageBox.critical(
            father,
            '错误',
            info)

if __name__ == '__main__':
    a = UIC()
    print(a.nowpath)