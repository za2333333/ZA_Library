# -*- coding: UTF-8 -*-
import sys
import xlrd2
import random
from PySide2.QtWidgets import QApplication, QButtonGroup, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtCore
from PySide2.QtWidgets import QFileDialog

class Stats:
    def __init__(self):
        # 初始化部分参数
        self.filePath = ['', '']
        self.modeid = ''

        self.ui = QUiLoader().load('UI/UI1.ui')
        self.ui.select_file_Button.clicked.connect(self.selectfile)
        self.intiUi()
        self.ui.pushButton.clicked.connect(self.openexcal)

    def openexcal(self):
        if (self.filePath == ['', '']) or (self.modeid == '') or ('xlsx' not in self.filePath[0]):
            QMessageBox.critical(self.ui,
                              '错误！',
                              f'请选择单词文件或默写方式'
                              )
        else:
            self.read_excal()
            self.stats2 = Stats2(self.wordlist,self.modeid)
            self.stats2.ui2.show()

    def intiUi(self):
        btn_group = QButtonGroup(self.ui)
        btn_group.addButton(self.ui.CNButton, 0)
        btn_group.addButton(self.ui.JPButton, 1)
        btn_group.buttonClicked.connect(self.rbtnClicked)

    def rbtnClicked(self, item):
        self.modeid = item.group().checkedId()
        # print("选中项的id为：", item.group().checkedId())  # 选中选在 选项组中的id。
        # print("选中项的名称为：%s\n" % item.text())  # 选中项的文本内容

    def selectfile(self):
        self.filePath = QFileDialog.getOpenFileName(
            self.ui,  # 父窗口对象
            "选择你要上传的单词表",  # 标题
            r"/Users/zhuan/Desktop/乱七八糟/",  # 起始目录
            "表格类型 (*.xlsx)"  # 选择类型过滤项，过滤内容在括号中
        )
        filename = self.filePath[0].split('/')[-1]
        self.ui.lineEdit.setText(filename)
        # print(self.filePath)

    def read_excal(self):
        self.wordlist = []
        value = xlrd2.open_workbook(self.filePath[0])
        book = value.sheet_by_index(0)  # 通过索引定位到Excel表格的第一张
        for item in range(1, book.nrows):   # 因为第一行是属性，所以不使用，从索引1开始循环第一张的所有单元格
            self.wordlist.append(book.row_values(item)) # 返回切片单元格的值添加到列表lists中
        # print(self.wordlist)

class Stats2():
    def __init__(self,wordlist,modeid):
        # 初始化部分参数
        self.jm1,self.ry1,self.zw1,self.sd1 = '','','',''
        self.wordlist = wordlist
        self.modeid = modeid
        self.ui2 = QUiLoader().load('UI/UI2.ui')
        self.ui2.Button1.clicked.connect(self.checkword)
        self.ui2.Button2.clicked.connect(self.nextword)

    def checkword(self):
        if self.sd1 == '':
            QMessageBox.warning(
                self.ui2,
                '警告',
                '请先确认你要验证的单词！')
        else:
            self.ui2.JM2.setText(self.jm1)
            self.ui2.RY2.setText(self.ry1)
            self.ui2.ZW2.setText(self.zw1)
            self.ui2.SD2.setText(self.sd1)

    def nextword(self):
        self.dele()
        if len(self.wordlist) != 0:
            num = random.randint(0, (len(self.wordlist)-1))
            self.jm1 = self.wordlist[num][0]
            self.ry1 = self.wordlist[num][1]
            self.zw1 = self.wordlist[num][2]
            self.sd1 = str(self.wordlist[num][3]).split('.')[0]
            self.wordlist.pop(num)
            # print(len(self.wordlist))

            if self.modeid == 0:
                self.ui2.ZW1.setEnabled(False)
                self.ui2.ZW1.setText(self.zw1)
            elif self.modeid == 1:
                self.ui2.RY1.setEnabled(False)
                self.ui2.RY1.setText(self.ry1)

        else:
            choice = QMessageBox.question(
                self.ui2,
                '已结束：',
                '全部单词已验证结束，是否关闭程序')

            if choice == QMessageBox.Yes:
                sys.exit()
            elif choice == QMessageBox.No:
                self.ui2.Button2.setEnabled(False)

    def dele(self):
        textlist = [self.ui2.JM1,self.ui2.RY1,self.ui2.ZW1,self.ui2.SD1,
                    self.ui2.JM2,self.ui2.RY2,self.ui2.ZW2,self.ui2.SD2]
        for item in textlist:
            item.clear()

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()