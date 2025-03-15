# -*- coding: UTF-8 -*-
import asyncio
import re
import shutil
from threading import Thread
from PySide6.QtCore import QObject, Signal
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import aiohttp
import aiofiles
import mkdir
# 导入sys
import sys
# 任何一个PySide界面程序都需要使用QApplication
# 我们要展示一个普通的窗口，所以需要导入QWidget，用来让我们自己的类继承
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QTabWidget, QMessageBox, QTextBrowser,QPushButton
# 导入我们生成的界面
from UI1 import Ui_Form
from log_print import *

# 自定义信号源对象类型，一定要继承自 QObject
class MySignals(QObject):
    # 定义一种信号，两个参数 类型分别是： QTextBrowser 和 字符串
    # 调用 emit方法 发信号时，传入参数 必须是这里指定的 参数类型
    text_print = Signal(str)
    set_enable = Signal(int)
    show_critical = Signal(str)
    nexttab = Signal(int)

# 实例化
global_ms = MySignals()

# 继承QWidget类，以获取其属性和方法
class MyWidget(QWidget):
    '''d定义UI的基础控件和自定义控件'''
    def __init__(self):
        #__init__为，初始化函数，会先执行
        super().__init__()
        # 设置界面为我们生成的界面
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.tab1()
        self.tab2()
        self.tab3()
        # 设置默认显示的tab页
        self.ui.tabWidget.setCurrentIndex(0)
        # 自定义信号的处理函数，链接信号与槽
        global_ms.text_print.connect(self.print_to_textbrowser)
        global_ms.set_enable.connect(self.change_enable)
        global_ms.show_critical.connect(self.append_critical)
        global_ms.nexttab.connect(self.go_tab)

    def tab1(self):
        '''定义tab1中的控件属性和功能'''
        self.ui.tab_2.setEnabled(False)
        self.ui.tab_3.setEnabled(False)
        self.ui.textBrowser1_1.setText(
            '1、单个相册的照片数量不能超过1000！\n'
            '2、相册的总数不能超过40！\n'
            '3、存放的路径尽量为空目录\n'
            '4、只支持照片的下载，视频会被下载为预览图片！\n'
            '5、请保证该程序所在目录下的空间足够大！\n'
            '6、如果因网络原因下载终止，请重新运行此程序！\n'
            '7、照片数量较大的话，可能会被腾讯端屏蔽，可以多试几次'
        )
        self.ui.pushButton1_1.clicked.connect(self.next2)

    def tab2(self):
        '''定义tab2中的控件属性和功能'''
        self.ui.pushButton2_1.clicked.connect(self.selectfile)
        self.ui.pushButton2_2.clicked.connect(self.checkdata)

    def tab3(self):
        '''定义tab2中的控件属性和功能'''
        self.ui.textBrowser3_1.setText(
            '1、点击确认已读按钮后，会在Chrome浏览器中打开QQ空间登录页面\n'
            '2、在QQ空间登录页面中登录你的QQ，等待浏览器跳转至你的空间并完全加载后，再点击确认登录按钮\n'
            '3、点击确认登录后会开始下载相册，期间请不要关闭相关窗口\n')
        self.ui.pushButton3_2.setEnabled(False)
        self.ui.pushButton3_1.clicked.connect(self.loginUI)
        self.ui.pushButton3_2.clicked.connect(self.start_download)

    @decorate_log
    def print_to_textbrowser(self,text):
        '''自定义信号1的关联功能，用于向文本框中添加文本内容'''
        self.ui.textBrowser5_1.setText(text)
        self.ui.textBrowser5_1.ensureCursorVisible()  # ensureCursorVisible()用于确保光标可见
        if self.failnum == 1:
            QMessageBox.critical(
                    self.ui.tab_5,
                    '错误',
                    text)
            self.driver.quit()
            sys.exit()

    @decorate_log
    def change_enable(self,num):
        '''自定义信号2的关联功能，用于改变控件的enable状态'''
        # fb.setEnabled(num)
        if num == 1:
            self.ui.pushButton3_2.setEnabled(True)
        else:
            self.ui.pushButton3_2.setEnabled(False)

    @decorate_log
    def append_critical(self,text):
        '''自定义信号3的关联功能，用于打开异常提示弹窗'''
        QMessageBox.critical(
            self.ui.tab_5,
            '错误',
            text)

    @decorate_log
    def go_tab(self, num):
        '''自定义信号4的关联功能，用于跳转tab页'''
        self.ui.tabWidget.setCurrentIndex(num)

    @decorate_log
    def next2(self):
        '''tab1中确认按钮关联的功能，用于跳转到tab2'''
        self.ui.tab_2.setEnabled(True)
        self.ui.tab_1.setEnabled(False)
        self.ui.tabWidget.setCurrentIndex(1)

    @decorate_log
    def selectfile(self):
        '''tab2中浏览按钮关联的功能，用于打开文件选择的弹窗'''
        self.albumPath = QFileDialog.getExistingDirectory(self.ui.tab_2, "选择存储路径")
        self.ui.lineEdit2_1.setText(self.albumPath)

    @decorate_log
    def checkdata(self):
        '''tab2中确认按钮关联的功能，用于检查文件是否选择，QQ账号是否填写'''
        if (self.ui.lineEdit2_1.text() == '') or (self.ui.lineEdit2_2.text() == ''):
            QMessageBox.critical(self.ui.tab_2,
                              '错误！',
                              f'请选择存储路径并填写你的QQ账号'
                              )
        else:
            self.ui.tab_2.setEnabled(False)
            self.ui.tab_3.setEnabled(True)
            self.ui.tabWidget.setCurrentIndex(2)

    @decorate_log
    def loginUI(self):
        '''tab3中确认已读按钮关联的功能，用于打开浏览器'''
        self.ui.pushButton3_1.setEnabled(False)
        self.usernum = self.ui.lineEdit2_2.text()
        self.driver = webdriver.Chrome()

        @decorate_log
        def threadFunc1():
            '''打开QQ空间登录页面'''
            # 通过Signal的emit触发执行 主线程里面的处理函数
            # emit参数和定义Signal的数量、类型必须一致
            # 调用登录函数
            self.login(self.usernum, self.driver)
            global_ms.set_enable.emit(1)

        # 创建线程在浏览器中打开QQ空间
        thread = Thread(target=threadFunc1)
        thread.start()

    # @decorate_log
    # def loginUI2(self,usernum):
    #     self.driver = webdriver.Chrome()
    #     # global drver
    #     self.login(usernum,self.driver)
    #     self.ui.pushButton3_2.setEnabled(True)

    @decorate_log
    def start_download(self):
        '''tab3中确认登录按钮关联功能，修改UI，实现照片下载流程'''
        QMessageBox.warning(
            self.ui.tab_3,
            '警告',
            '开始下载，请不要关闭当前窗口和浏览器窗口！！！')
        self.ui.pushButton3_2.setEnabled(False)
        self.ui.tabWidget.setCurrentIndex(3)
        self.neednum = 0    # 需要下载的数量
        self.downnum = 0    # 下载数量
        self.sucnum = 0     # 成功下载数量
        self.failnum = 0    # 失败下载数量

        @decorate_log
        def mainUI(usernum):
            '''实现照片下载流程'''
            # 删除data文件夹
            mkdir.del_dir('./data')
            # 创建data文件夹
            mkdir.cret_dir('./data')
            # 获取动态加载后的空间相册代码
            self.get_page(self.driver)
            # print(self.page)
            # 获取cookie
            self.get_cookie(self.driver)
            # print(self.cookielist)
            self.driver.minimize_window()
            # 获取URL中的必要参数
            self.get_g_tk(self.driver)
            print(self.g_tk)
            # 从页面代码中提取相册的信息
            self.get_album_list(self.page)
            # print(self.list1)
            # 提取所有相册的URL
            self.get_url(self.list1, self.g_tk, usernum)
            # print(self.urllist)
            headers = {
                "cookie": self.cookielist
            }
            headers.update({'Upgrade':'http/1.1'})
            # print(headers)
            # 获取各个相册网页的源代码，提取所有照片的信息
            asyncio.run(self.get_photo(self.urllist, headers, self.list1))
            print(self.neednum)
            # 获取所有照片信息分析并下载写入
            try:
                asyncio.run(self.get_photodata())
                global_ms.text_print.emit('下载完成！')
                global_ms.nexttab.emit(4)
                # self.ui.textBrowser5_1.setText('下载完成！')
                # 跳转到tab5
                # self.ui.tabWidget.setCurrentIndex(4)
            # 二次拦截，防止除网络原因外导致的下载失败
            except Exception as ression:
                exc_type, exc_value, exc_traceback_obj = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback_obj, limit=5, file=sys.stdout)
                print(f'报错：{ression}，下载失败，停止下载！')
                global_ms.nexttab.emit(4)
                if (self.ui.textBrowser5_1.toPlainText() == '下载失败！'):
                    pass
                else:
                    global_ms.show_critical.emit(f'失败原因：{ression}')
                    global_ms.text_print.emit('下载失败！')
                    sys.exit()
                # global_ms.text_print.emit('下载失败！')
                # global_ms.nexttab.emit(4)
                # global_ms.show_critical.emit(f'失败原因：{ression}')
                # self.ui.tabWidget.setCurrentIndex(4)
                # QMessageBox.critical(
                #     self.ui.tab_5,
                #     '错误',
                #     f'报错：{ression}，下载失败，停止下载！')
                # self.ui.textBrowser5_1.setText('下载失败，停止下载')
                sys.exit()
            self.driver.quit()
            # 清空缓存数据
            # mkdir.del_dir('./data')

        thread = Thread(target=mainUI,
                        args=(self.usernum,))
        thread.start()

    # 登录模块
    @decorate_log
    def login(self,usernum, driver):
        url = (f'https://user.qzone.qq.com/{usernum}/4')
        driver.get(url)
        sleep(15)

    # 获取cookie
    @decorate_log
    def get_cookie(self,driver):
        cookies = driver.get_cookies()
        self.cookielist = ';'.join([cookie['name'] + '=' + cookie['value'] for cookie in cookies])
        # return cookielist

    # 获取动态加载后的空间相册代码
    @decorate_log
    def get_page(self,driver):
        driver.set_window_size(480, 800)
        js = "window.scrollTo(0,document.body.scrollHeight)"
        # 执行JavaScript代码来控制浏览器滚动条的位置
        driver.execute_script(js)
        sleep(5)
        f1 = driver.find_element(by=By.XPATH, value='//*[@id="tphoto"]')
        driver.switch_to.frame(f1)
        sleep(1)
        # 获取动态加载后的页面代码
        self.page = driver.page_source
        # return page

    # 获取所有相册信息
    @decorate_log
    def get_album_list(self,page):
        page_text = BeautifulSoup(page, "html.parser")
        album_list = page_text.find_all('div', class_="bg bor3 mod-album js-album-item js-album-transition")
        self.list1 = [] #存放所有相册信息
        for albums in album_list:
            # 获取相册ID、相册名称、相册照片总数
            id, name, num = albums.get('data-id'), albums.get('data-name'), albums.get('data-total')
            datalist = []   # 临时存放相册信息
            if (int(num) > 500):    # 处理相册照片数量大于500的
                # 将单个相册信息存放在datalist中，先存放500条，再将多出的存放在新的记录中
                datalist.extend([id, name, 500])
                # 将单个相册信息存放在总的相册信息列表中
                self.list1.append(datalist)
                # 清空临时列表
                datalist = []
                # 计算除去500后的照片数量
                num = int(num) - 500
            datalist.extend([id, name, num])
            self.list1.append(datalist)
        # return list1

    # 处理URL中的必要信息
    @decorate_log
    def get_g_tk(self,driver):
        self.g_tk = driver.execute_script('return QZONE.FP.getACSRFToken()')
        # return g_tk

    # 处理所有相册的URL
    @decorate_log
    def get_url(self,lists, g_tk, usernum):
        self.urllist = []   # 存放所有相册的URL
        olddata = [0]
        for data in lists:
            if (data[0] == olddata[0]):
                # 判断当前相册信息是否为上一个相册的补充，即与上一个相册名称相同，是超过500条照片的相册，当照片数量超过500时，URL发生变化
                url = (
                            "https://h5.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/cgi_list_photo?g_tk=%s&callback=shine0_Callback&t=826272405&mode=0&idcNum=4&hostUin=%s&topicId=%s&noTopic=0&uin=%s&pageStart=500&pageNum=%d&skipCmtCount=0&singleurl=1&batchId=&notice=0&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone&plat=qzone&outstyle=json&format=jsonp&json_esc=1&question=&answer=&callbackFun=shine0&_=1668081263010" % (
                    g_tk, usernum, data[0], usernum, int(data[2])))
            else:
                url = (
                            "https://h5.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/cgi_list_photo?g_tk=%s&callback=shine0_Callback&t=826272405&mode=0&idcNum=4&hostUin=%s&topicId=%s&noTopic=0&uin=%s&pageStart=0&pageNum=%d&skipCmtCount=0&singleurl=1&batchId=&notice=0&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone&plat=qzone&outstyle=json&format=jsonp&json_esc=1&question=&answer=&callbackFun=shine0&_=1668081263010" % (
                    g_tk, usernum, data[0], usernum, int(data[2])))
            self.urllist.append(url)
            olddata = data
        # return urllist

    # 将所有相册信息写入文件中
    # @decorate_log
    async def write_url(self,url, headers, list1, session):
        async with session.get(url, headers=headers, verify_ssl=False) as resp:
            async with aiofiles.open(f'./data/{list1[1]}data.txt', mode='a+') as f:
                page = await resp.text()
                # print(page)
                if list1[1] == "自古华山一条路":
                    print("123123123")
                else:
                    pass
                obj = re.compile(r'"lloc" : "(?P<lloc>.*?)".*?'
                                 r'"name" : "(?P<name>.*?)".*?'
                                 r'"raw" : "(?P<url>.*?)",.*?'
                                 r'"uploadtime" : "(?P<time>.*?)",.*?'
                                 r'"url" : "(?P<url1>.*?)",', re.S)
                # obj = re.compile(r'"raw" : "(?P<url>.*?)",.*?'
                #                  r'"rawshoottime" : "(?P<time>.*?)",.*?'
                #                  r'"url" : "(?P<url1>.*?)",', re.S)
                photodata_list = obj.finditer(page)

                pto_num = 0;
                for photo in photodata_list:
                    pto_num += 1
                    self.neednum += 1   # 需要下载的照片数量+1
                    if photo.group('url') == '':
                        photourl = photo.group('url1')
                    else:
                        photourl = photo.group('url')
                    # 照片信息在文件中的命名
                    photoname = photo.group('time').replace(' ', '-').replace(':', '-')
                    photo = ("%s %s %s\n" % (photoname, photourl, list1[1]))
                    # print(photo.group('url1'),photo.group('time'),photo.group('name'))
                    # print(photoname, photourl, list1[1])
                    await f.write(photo)
                print(f"{list1[1]}' '{pto_num}'")
    # 请求所有相册的信息
    # @decorate_log
    async def get_photo(self,urllist, headers, list1):
        task = []
        timeout = aiohttp.ClientTimeout(total=600)  # 将超时时间设置为600秒
        connector = aiohttp.TCPConnector(limit=50)  # 将并发数量降低
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        # async with aiohttp.ClientSession() as session:
            i = 0
            for url in urllist:
                task.append(asyncio.create_task(self.write_url(url, headers, list1[i], session)))
                i += 1
            await asyncio.wait(task)

    # 下载照片并保存
    # @decorate_log
    async def download_photos(self,photolist, session):
        if self.failnum >0: # 先判断失败数，有失败直接PASS
            pass
        else:
            async with session.get(url=photolist[1], verify_ssl=False) as resp:
                if not (os.path.exists(f'{self.albumPath}/{photolist[2]}/')):
                    os.mkdir(f'{self.albumPath}/{photolist[2]}/')
                # print(photolist[2])
                async with aiofiles.open(f'{self.albumPath}/{photolist[2]}/{photolist[0]}', mode='xb') as f:
                    # await f.write(await resp.content.read())

                    '''下面这段代码会导致多个报错弹窗出现'''
                    try:
                        self.downnum += 1
                        # print(f'下载数为{self.downnum}')
                        await f.write(await resp.content.read())
                        self.sucnum += 1
                        print(f'成功数为{self.sucnum}')
                    except Exception as ression:
                        print(f'下载失败，停止下载！\n{ression}')
                        self.failnum += 1
                        print(f'失败数为{self.failnum}')
                        # 失败后直接PASS，不再浪费时间请求和处理失败的后续
                        pass

    # 下载照片并保存,方式2，传参不同，根据列表下标索引
    # @decorate_log
    async def download_photos_index(self, photo_list, session):
        try:
            async with session.get(url = photo_list[1], verify_ssl=False) as resp:
                if not (os.path.exists(f'{self.albumPath}/{photo_list[2]}/')):
                    os.mkdir(f'{self.albumPath}/{photo_list[2]}/')
                # print(photo_list[2])
                async with aiofiles.open(f'{self.albumPath}/{photo_list[2]}/{photo_list[0]}', mode='wb') as f:
                    # await f.write(await resp.content.read())

                    '''下面这段代码会导致多个报错弹窗出现'''
                    try:
                        self.downnum += 1
                        # print(f'下载数为{self.downnum}')
                        data = await resp.content.read();
                        if len(data) < 3000 and photo_list[2] != "说说和日志相册":
                            # print(f'图片异常，停止下载！\n')
                            self.failnum += 1
                            self.fail_photolist.append(photo_list)  # 将失败的照片信息添加进入失败列表
                        else:
                            await f.write(data)
                            self.sucnum += 1
                            print(f'成功数为{self.sucnum}')
                    except Exception as ression:
                        # print(f'下载失败，停止下载！\n{ression}')
                        self.failnum += 1
                        self.fail_photolist.append(photo_list)  # 将失败的照片信息添加进入失败列表
                        # print(f'失败数为{self.failnum}')
                        # 失败后直接PASS，不再浪费时间请求和处理失败的后续
                        pass
        except asyncio.exceptions.TimeoutError:
            self.failnum += 1
            self.fail_photolist.append(photo_list)  # 将失败的照片信息添加进入失败列表
            # print(f'失败数为{self.failnum}')
            # print(f"The request to '{photo_list[0]}'  '{photo_list[1]}'  '{photo_list[2]}' has been timed out after waiting for too long.")
            return False

        except Exception as ex:
            self.failnum += 1
            self.fail_photolist.append(photo_list)  # 将失败的照片信息添加进入失败列表

            # print(f"Some other errors happened during fetching the photo '{photo_list[0]}'  '{photo_list[1]}'  '{photo_list[2]}': {str(ex)}.")
            return False

    # 提取照片信息
    # @decorate_log
    async def get_photodata(self):
        dirlist = os.listdir('./data/')
        self.photoslist = [] # 存放所有照片信息
        self.fail_photolist = [] # 存放所有失败照片信息
        # 读取data文件夹下所有文件信息，并过滤掉不是txt的文件
        for dirone in dirlist:
            if ('.txt' not in dirone):  # 遍历每个txt文件
                continue
            with open(f'./data/{dirone}', mode='r', encoding='utf-8') as f:
                photolist = []  # 存放一条照片信息
                num = 1
                for line in f.readlines():  # 读取txt文件的每一行
                    linelist = line.split(' ')  # 以空格切割
                    photoname = ('%s-%d.png' % (linelist[0], num))
                    num += 1
                    # 存放单条照片信息：照片命名 照片下载URL 所在相册名称 状态标志位(0为未下载 1为已下载)
                    photolist.extend([photoname.strip(), linelist[1], linelist[2].strip()])
                    self.photoslist.append(photolist)
                    photolist = []
            # print(f"'{dirone}' nums is '{num}'")

        # 协程任务创建和执行
        task = []
        timeout = aiohttp.ClientTimeout(total=120)  # 将超时时间设置为600秒
        connector = aiohttp.TCPConnector(limit=1000)  # 将并发数量降低
        # async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
        async with aiohttp.ClientSession() as session:
            for each in self.photoslist:
                # task.append(asyncio.create_task(self.download_photos(each, session)))
                task.append(asyncio.create_task(self.download_photos_index(each, session)))
            await asyncio.wait(task)
            # draftlist = self.photoslist[0]
                # photoslist = [] # 下载完一个相册后，将相册列表置空，开始下载下一个相册

        # 以下部分为重下载的代码，可能会和上面的有重复的地方，合并时注意！
        while self.failnum: # 判断刚才下载的失败数，不为0时，则重新下载,写死，只要有失败项就重新下载
            # print(f'{self.failnum,}\n{self.albumPath}/{draftlist[2]}/') # {photolist[2]}这个报错，检查一下
            self.failnum = 0    # 将失败数置空，开始重新下载
            self.photoslist = []  # 将相册列表置空，准备存放失败的照片信息
            self.photoslist = self.fail_photolist   # 存放失败的照片信息
            self.fail_photolist = []  # 将失败的相册列表置空

            task = []
            timeout = aiohttp.ClientTimeout(total=120)  # 将超时时间设置为600秒
            connector = aiohttp.TCPConnector(limit=1000)  # 将并发数量降低
            # async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            async with aiohttp.ClientSession() as session:
                for each in self.photoslist:
                    # task.append(asyncio.create_task(self.download_photos(each, session)))
                    task.append(asyncio.create_task(self.download_photos_index(each, session)))
                await asyncio.wait(task)
        self.photoslist = []  # 下载完一个相册后，将相册列表置空，开始下载下一个相册

# 程序入口
if __name__ == "__main__":
    # 初始化QApplication，界面展示要包含在QApplication初始化之后，结束之前
    app = QApplication(sys.argv)

    # 初始化并展示我们的界面组件
    window = MyWidget()
    window.show()

    # 结束QApplication
    sys.exit(app.exec())