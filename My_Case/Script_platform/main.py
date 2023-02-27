# -*- coding: UTF-8 -*-
import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtUiTools import QUiLoader
from PySide2 import QtCore
from applescript import tell

class Stats:

    def __init__(self):
        self.ui = QUiLoader().load('UI/脚本平台draft.ui')
        scriplist=['相册下载','文件搜索']
        self.scriptdir={'相册下载':'需要MAC系统',
                        '文件搜索':'需要WINDOWS系统'}
        self.scritppath = {'相册下载':'python /Users/Github_Library/My_Case/QQSpace_Album_Download/main.py',
                          '文件搜索':'python /Users/Github_Library/My_Case/Windows_SearchFile/SearchFile.py'}
        self.ui.comboBox_select_scipt.addItems(scriplist)
        self.ui.textBrowser_careful_content.append('需要MAC系统')
        self.ui.comboBox_select_scipt.currentIndexChanged.connect(self.showcarefultxt)
        self.ui.pushButton.clicked.connect(self.Execute_script)

    def showcarefultxt(self):
        self.ui.textBrowser_careful_content.clear()
        name = self.ui.comboBox_select_scipt.currentText()
        self.ui.textBrowser_careful_content.append(self.scriptdir[name])

    def Execute_script(self):
        name = self.ui.comboBox_select_scipt.currentText()
        tell.app('Terminal', 'do script" ' + self.scritppath[name] + '"', background=True)
        print(f'开始执行{name}脚本')
        sys.exit()

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    stats = Stats()
    stats.ui.show()
    app.exec_()