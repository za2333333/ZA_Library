# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI1.ui'
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
        Form.resize(401, 313)
        self.horizontalLayout_4 = QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CNButton = QRadioButton(Form)
        self.CNButton.setObjectName(u"CNButton")

        self.horizontalLayout.addWidget(self.CNButton)

        self.JPButton = QRadioButton(Form)
        self.JPButton.setObjectName(u"JPButton")

        self.horizontalLayout.addWidget(self.JPButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.select_file_Button = QPushButton(Form)
        self.select_file_Button.setObjectName(u"select_file_Button")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_file_Button.sizePolicy().hasHeightForWidth())
        self.select_file_Button.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.select_file_Button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u5355\u8bcd\u8bb0\u5fc6", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u4f60\u8981\u9ed8\u5199\u5355\u8bcd\u7684\u65b9\u5f0f\uff1a", None))
        self.CNButton.setText(QCoreApplication.translate("Form", u"\u770b\u4e2d\u6587\u5199\u65e5\u6587", None))
        self.JPButton.setText(QCoreApplication.translate("Form", u"\u770b\u65e5\u6587\u5199\u4e2d\u6587", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u4e2d\u5355\u8bcd\u8868\u6587\u4ef6\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\uff1a", None))
        self.select_file_Button.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
    # retranslateUi

