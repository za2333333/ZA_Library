# # -*- coding:utf-8 -*-
# from PySide6.QtWidgets import QMainWindow, QButtonGroup
# from PySide6 import QtWidgets
# from PySide6.QtCore import Signal
# import sys
# from uimain import Ui_MainWindow  # 导入主窗口的UI代码
#
#
# class MainWindow(QMainWindow):
#     main_Signal = Signal(str)
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#         self.intiUi()
#
#     # # 初始化按钮事件
#     ########################################################################
#     def intiUi(self):
#         btn_group = QButtonGroup(self)
#         btn_group.addButton(self.ui.rbtn1, 0)
#         btn_group.addButton(self.ui.rbtn2, 1)
#         btn_group.buttonClicked.connect(self.rbtnClicked)
#
#     # # btn_group绑定的槽函数，item是btn_group绑定的槽函数传过来的信号
#     ########################################################################
#     def rbtnClicked(self, item):
#         print("选中项的id为：", item.group().checkedId())  # 选中选在 选项组中的id。
#         print("选中项的名称为：%s\n" % item.text())  # 选中项的文本内容
#         self.ui.textEdit.append("当前选中的按钮ID是：{}".format(item.group().checkedId()))
#         self.ui.textEdit.append("当前选中的按钮名称：{}".format(item.text()))
#
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     root = MainWindow()
#     root.show()
#     sys.exit(app.exec())

# -*- coding: UTF-8 -*-
from time import sleep

import xlrd2
import random
from PySide2.QtWidgets import QApplication, QButtonGroup, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtCore
from PySide2.QtWidgets import QFileDialog

class Stats2():
    def __init__(self):
        self.wordlist = [['ちゅうごくじん', '中国人', '中国人', 11100.0], ['にほんじん', '日本人', '日本人', 1110.0], ['かんこくじん', '韓国人', '韩国人', 11100.0], ['アメリカじん', 'アメリカ人', '美国人', 11110.0], ['フランスじん', 'フランス人', '法国人', 11100.0], ['がくせい', '学生', '（大）学生', 111.0], ['せんせい', '先生', '老师', 110.0], ['りゅうがくせい', '留学生', '留学生', 11000.0], ['きょうじゅ', '教授', '教授', 111.0], ['しゃいん', '社員', '职工、员工', 1100.0], ['かいしゃいん', '会社員', '公司员工', 11100.0], ['てんいん', '店員', '店员', 111.0], ['けんしゅうせい', '研修生', '进修生', 111000.0], ['きぎょう', '企業', '企业', 1000.0], ['だいがく', '大学', '大学', 111.0], ['ちち', '父', '(我)父亲', 1.0], ['かちょう', '課長', '科长', 111.0], ['しゃちょう', '社長', '总经理、社长', 111.0], ['でむかえ', '出迎え', '迎接', 111.0], ['あのひと', 'あの人', '那个人', ''], ['わたし', '', '我', 11.0], ['あなた', '', '你', 10.0], ['どうも', '', '非常，很', 100.0], ['はい', '', '哎，是（应答）；是的', 10.0], ['いいえ', '', '不，不是', 11.0], ['あう', '', '哎，哎呀', 0.0], ['り', '李', '李', 0.0], ['おう', '王', '王', 10.0], ['ちょう', '張', '张', 110.0], ['もり', '森', '森', 1.0], ['はやし', '林', '林', 11.0], ['おの', '小野', '小野', 1.0], ['よしだ', '吉田', '吉田', 11.0], ['たなか', '田中', '田中', 11.0], ['なかむら', '中村', '中村', 111.0], ['たろう', '太郎', '太郎', 100.0], ['キム', '金', '金', 10.0], ['デユポン', '', '迪蓬', 1100.0], ['スミス', '', '史密斯', 100.0], ['ジョンソン', '', '约翰逊', 11000.0], ['ちゅうごく', '中国', '中国', 1100.0], ['とうきょうだいがく', '東京大学', '东京大学', 11111000.0], ['ぺきんだいがく', '北京大学', '北京大学', 111000.0], ['ジエーしーきかく', 'JC企画', 'JC策划公司', 111100.0], ['ペキンりょこうしゃ', '北京旅行社', '北京旅行社', 11111000.0], ['にっちゅうしょうじ', '日中商社', '日中商社', 11111100.0]]
        self.modeid = 0
        self.ui2 = QUiLoader().load('UI/UI2.ui')
        self.ui2.Button2.clicked.connect(self.showword)

    def showword(self):
        num = random.randint(0, (len(self.wordlist)-1))
        print(len(self.wordlist),num)
        self.jm1 = self.wordlist[num][0]
        self.ry1 = self.wordlist[num][1]
        self.zw1 = self.wordlist[num][2]
        self.sd1 = self.wordlist[num][3]
        # self.ui2.Button2.setEnabled(False)
        self.wordlist.pop(num)
        if self.modeid == 0:
            self.ui2.ZW1.setText(self.zw1)

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    stats = Stats2()
    stats.ui2.show()
    app.exec_()