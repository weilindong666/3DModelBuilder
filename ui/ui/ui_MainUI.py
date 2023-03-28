# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainUIUSONgQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui.ui.MyListWidget import MyListWidget
from ui.ui.MDI_subWindows import MyMdiWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1360, 898)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.action_import_single_file = QAction(MainWindow)
        self.action_import_single_file.setObjectName(u"action_import_single_file")
        self.action_import_ROI = QAction(MainWindow)
        self.action_import_ROI.setObjectName(u"action_import_ROI")
        self.action_import_model = QAction(MainWindow)
        self.action_import_model.setObjectName(u"action_import_model")
        self.action_export_ROI = QAction(MainWindow)
        self.action_export_ROI.setObjectName(u"action_export_ROI")
        self.action_export_model = QAction(MainWindow)
        self.action_export_model.setObjectName(u"action_export_model")
        self.action_import_folder = QAction(MainWindow)
        self.action_import_folder.setObjectName(u"action_import_folder")
        self.action_go_back = QAction(MainWindow)
        self.action_go_back.setObjectName(u"action_go_back")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.listWidget = MyListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")

        self.horizontalLayout.addWidget(self.listWidget)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.widget = MyMdiWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")

        self.horizontalLayout.addWidget(self.widget)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(2, 8)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1360, 23))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menu)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menu)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action_go_back)
        self.menu_2.addAction(self.action_import_single_file)
        self.menu_2.addAction(self.action_import_folder)
        self.menu_2.addAction(self.action_import_ROI)
        self.menu_2.addAction(self.action_import_model)
        self.menu_3.addAction(self.action_export_ROI)
        self.menu_3.addAction(self.action_export_model)
        self.toolBar.addAction(self.action_import_single_file)
        self.toolBar.addAction(self.action_import_folder)
        self.toolBar.addAction(self.action_go_back)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_import_single_file.setText(QCoreApplication.translate("MainWindow", u"\u5355\u4e2a\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.action_import_single_file.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u5355\u4e2a\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.action_import_ROI.setText(QCoreApplication.translate("MainWindow", u"ROI", None))
#if QT_CONFIG(tooltip)
        self.action_import_ROI.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165ROI", None))
#endif // QT_CONFIG(tooltip)
        self.action_import_model.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
#if QT_CONFIG(tooltip)
        self.action_import_model.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6a21\u578b", None))
#endif // QT_CONFIG(tooltip)
        self.action_export_ROI.setText(QCoreApplication.translate("MainWindow", u"ROI", None))
#if QT_CONFIG(tooltip)
        self.action_export_ROI.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u51faROI", None))
#endif // QT_CONFIG(tooltip)
        self.action_export_model.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
#if QT_CONFIG(tooltip)
        self.action_export_model.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6a21\u578b", None))
#endif // QT_CONFIG(tooltip)
        self.action_import_folder.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u5939", None))
#if QT_CONFIG(tooltip)
        self.action_import_folder.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6587\u4ef6\u5939", None))
#endif // QT_CONFIG(tooltip)
        self.action_go_back.setText(QCoreApplication.translate("MainWindow", u"\u8fd4\u56de", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

