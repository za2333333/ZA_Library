# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(559, 289)
        Form.setStyleSheet(u"QLabel#label_10{ \n"
"    color: red ;\n"
"    font-size:15px;\n"
"}\n"
"QLabel#label_11{ \n"
"    color: red ;\n"
"    font-size:15px;\n"
"}")
        self.horizontalLayout_11 = QHBoxLayout(Form)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.JM1 = QLineEdit(Form)
        self.JM1.setObjectName(u"JM1")

        self.horizontalLayout.addWidget(self.JM1)

        self.horizontalLayout.setStretch(1, 9)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.RY1 = QLineEdit(Form)
        self.RY1.setObjectName(u"RY1")

        self.horizontalLayout_2.addWidget(self.RY1)

        self.horizontalLayout_2.setStretch(1, 9)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.ZW1 = QLineEdit(Form)
        self.ZW1.setObjectName(u"ZW1")

        self.horizontalLayout_3.addWidget(self.ZW1)

        self.horizontalLayout_3.setStretch(1, 9)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.SD1 = QLineEdit(Form)
        self.SD1.setObjectName(u"SD1")

        self.horizontalLayout_4.addWidget(self.SD1)

        self.horizontalLayout_4.setStretch(1, 9)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Button1 = QPushButton(Form)
        self.Button1.setObjectName(u"Button1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Button1.sizePolicy().hasHeightForWidth())
        self.Button1.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.Button1)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_11.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_2.addWidget(self.label_11)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.JM2 = QLineEdit(Form)
        self.JM2.setObjectName(u"JM2")
        self.JM2.setEnabled(False)

        self.horizontalLayout_5.addWidget(self.JM2)

        self.horizontalLayout_5.setStretch(1, 9)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.RY2 = QLineEdit(Form)
        self.RY2.setObjectName(u"RY2")
        self.RY2.setEnabled(False)

        self.horizontalLayout_6.addWidget(self.RY2)

        self.horizontalLayout_6.setStretch(1, 9)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.ZW2 = QLineEdit(Form)
        self.ZW2.setObjectName(u"ZW2")
        self.ZW2.setEnabled(False)

        self.horizontalLayout_7.addWidget(self.ZW2)

        self.horizontalLayout_7.setStretch(1, 9)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.SD2 = QLineEdit(Form)
        self.SD2.setObjectName(u"SD2")
        self.SD2.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.SD2)

        self.horizontalLayout_8.setStretch(1, 9)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.Button2 = QPushButton(Form)
        self.Button2.setObjectName(u"Button2")
        sizePolicy.setHeightForWidth(self.Button2.sizePolicy().hasHeightForWidth())
        self.Button2.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.Button2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5355\u8bcd\u8bb0\u5fc6", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u4e66\u5199", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5047\u540d\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u65e5\u8bed\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4e2d\u6587\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u58f0\u8c03\uff1a", None))
        self.Button1.setText(QCoreApplication.translate("Form", u"\u9a8c\u8bc1", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u5bf9\u7167\u8868", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5047\u540d\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u65e5\u8bed\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u4e2d\u6587\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u58f0\u8c03\uff1a", None))
        self.Button2.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u4e2a", None))
    # retranslateUi

