# -*- coding: UTF-8 -*-
'''
@Time    : 2023/3/20 11:07
@Author  : 魏林栋
@Site    : 
@File    : UI_Master.py
@Software: PyCharm
'''
from ui.MainUI import MainUI


class UI_Master:

    def __init__(self, MySignals, Pool, Tools):
        self.MainUI = MainUI(MySignals, Pool, Tools)