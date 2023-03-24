# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OpenGLUIIHxkzK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui.ui.opengl_widget import openGL_Widget


class Ui_OpenGL_Form(object):
    def setupUi(self, OpenGL_Form):
        if not OpenGL_Form.objectName():
            OpenGL_Form.setObjectName(u"OpenGL_Form")
        OpenGL_Form.resize(1063, 793)
        self.verticalLayout = QVBoxLayout(OpenGL_Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = openGL_Widget(OpenGL_Form)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(OpenGL_Form)

        QMetaObject.connectSlotsByName(OpenGL_Form)
    # setupUi

    def retranslateUi(self, OpenGL_Form):
        OpenGL_Form.setWindowTitle(QCoreApplication.translate("OpenGL_Form", u"3D Model", None))
    # retranslateUi

