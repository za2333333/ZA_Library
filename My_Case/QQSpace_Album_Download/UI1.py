# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UI1.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(523, 352)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.verticalLayout_2 = QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label1_1 = QLabel(self.tab_1)
        self.label1_1.setObjectName(u"label1_1")

        self.verticalLayout_2.addWidget(self.label1_1)

        self.textBrowser1_1 = QTextBrowser(self.tab_1)
        self.textBrowser1_1.setObjectName(u"textBrowser1_1")

        self.verticalLayout_2.addWidget(self.textBrowser1_1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton1_1 = QPushButton(self.tab_1)
        self.pushButton1_1.setObjectName(u"pushButton1_1")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton1_1.sizePolicy().hasHeightForWidth())
        self.pushButton1_1.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButton1_1)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label2_1 = QLabel(self.tab_2)
        self.label2_1.setObjectName(u"label2_1")

        self.verticalLayout_3.addWidget(self.label2_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label2_2 = QLabel(self.tab_2)
        self.label2_2.setObjectName(u"label2_2")

        self.horizontalLayout_2.addWidget(self.label2_2)

        self.lineEdit2_1 = QLineEdit(self.tab_2)
        self.lineEdit2_1.setObjectName(u"lineEdit2_1")
        self.lineEdit2_1.setEnabled(False)

        self.horizontalLayout_2.addWidget(self.lineEdit2_1)

        self.pushButton2_1 = QPushButton(self.tab_2)
        self.pushButton2_1.setObjectName(u"pushButton2_1")
        sizePolicy.setHeightForWidth(self.pushButton2_1.sizePolicy().hasHeightForWidth())
        self.pushButton2_1.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.pushButton2_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label2_3 = QLabel(self.tab_2)
        self.label2_3.setObjectName(u"label2_3")

        self.verticalLayout_3.addWidget(self.label2_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label2_4 = QLabel(self.tab_2)
        self.label2_4.setObjectName(u"label2_4")

        self.horizontalLayout_3.addWidget(self.label2_4)

        self.lineEdit2_2 = QLineEdit(self.tab_2)
        self.lineEdit2_2.setObjectName(u"lineEdit2_2")

        self.horizontalLayout_3.addWidget(self.lineEdit2_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton2_2 = QPushButton(self.tab_2)
        self.pushButton2_2.setObjectName(u"pushButton2_2")
        sizePolicy.setHeightForWidth(self.pushButton2_2.sizePolicy().hasHeightForWidth())
        self.pushButton2_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.pushButton2_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_5 = QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label3_1 = QLabel(self.tab_3)
        self.label3_1.setObjectName(u"label3_1")

        self.verticalLayout_4.addWidget(self.label3_1)

        self.textBrowser3_1 = QTextBrowser(self.tab_3)
        self.textBrowser3_1.setObjectName(u"textBrowser3_1")

        self.verticalLayout_4.addWidget(self.textBrowser3_1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton3_1 = QPushButton(self.tab_3)
        self.pushButton3_1.setObjectName(u"pushButton3_1")

        self.horizontalLayout_5.addWidget(self.pushButton3_1)

        self.pushButton3_2 = QPushButton(self.tab_3)
        self.pushButton3_2.setObjectName(u"pushButton3_2")

        self.horizontalLayout_5.addWidget(self.pushButton3_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_6 = QVBoxLayout(self.tab_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label4_1 = QLabel(self.tab_4)
        self.label4_1.setObjectName(u"label4_1")

        self.verticalLayout_6.addWidget(self.label4_1)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_7 = QVBoxLayout(self.tab_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label5_1 = QLabel(self.tab_5)
        self.label5_1.setObjectName(u"label5_1")

        self.verticalLayout_7.addWidget(self.label5_1)

        self.textBrowser5_1 = QTextBrowser(self.tab_5)
        self.textBrowser5_1.setObjectName(u"textBrowser5_1")

        self.verticalLayout_7.addWidget(self.textBrowser5_1)

        self.tabWidget.addTab(self.tab_5, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u76f8\u518c\u4e0b\u8f7d", None))
        self.label1_1.setText(QCoreApplication.translate("Form", u"\u6ce8\u610f\u4e8b\u9879\uff1a", None))
        self.pushButton1_1.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u5df2\u8bfb\uff0c\u4e0b\u4e00\u6b65", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("Form", u"\u7b2c\u4e00\u6b65", None))
        self.label2_1.setText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9\u76f8\u518c\u5b58\u50a8\u6587\u4ef6\u5939\uff1a", None))
        self.label2_2.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u8def\u5f84\uff1a", None))
        self.pushButton2_1.setText(QCoreApplication.translate("Form", u"\u6d4f\u89c8", None))
        self.label2_3.setText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u4ee5\u4e0b\u4fe1\u606f\uff1a", None))
        self.label2_4.setText(QCoreApplication.translate("Form", u"QQ\u8d26\u53f7\uff1a", None))
        self.pushButton2_2.setText(QCoreApplication.translate("Form", u"\u786e\u5b9a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u7b2c\u4e8c\u6b65", None))
        self.label3_1.setText(QCoreApplication.translate("Form", u"\u6ce8\u610f\u4e8b\u9879\uff1a", None))
        self.pushButton3_1.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u5df2\u8bfb", None))
        self.pushButton3_2.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4\u767b\u5f55", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u7b2c\u4e09\u6b65", None))
        self.label4_1.setText(QCoreApplication.translate("Form", u"\u6b63\u5728\u4e0b\u8f7d\u4e2d\uff0c\u8bf7\u4e0d\u8981\u5173\u95ed\u7a97\u53e3\uff0c\u7b49\u5f85\u4e0b\u8f7d\u7ed3\u679c\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u7b2c\u56db\u6b65", None))
        self.label5_1.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d\u7ed3\u679c\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u7b2c\u4e94\u6b65", None))
    # retranslateUi

