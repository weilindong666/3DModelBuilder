# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageShowUIUXtcFC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ImageShow_Form(object):
    def setupUi(self, ImageShow_Form):
        if not ImageShow_Form.objectName():
            ImageShow_Form.setObjectName(u"ImageShow_Form")
        ImageShow_Form.resize(941, 652)
        self.verticalLayout = QVBoxLayout(ImageShow_Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(ImageShow_Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(ImageShow_Form)

        QMetaObject.connectSlotsByName(ImageShow_Form)
    # setupUi

    def retranslateUi(self, ImageShow_Form):
        ImageShow_Form.setWindowTitle(QCoreApplication.translate("ImageShow_Form", u"Image Show", None))
        self.label.setText("")
    # retranslateUi

