'''import easygui as g
import sys

while 1:
    g.msgbox("嗨，欢迎进入第一个页面小游戏^_^")

    msg = "请问你希望在朱安这儿学习到什么呢？？？"
    title = "小游戏互动"
    choices = ["谈恋爱","编程","琴棋书画"]

    choice = g.choicebox(msg,title,choices)

    # 注意，msgbox的参数是一个字符串
    # 如果用户选择Cancel，该函数返回None
    g.msgbox("你的选择是：" + str(choice),"结果")

    msg = "你希望重新开始小游戏吗？"
    title = "请选择"

    # 弹出一个Continue/Cancel对话框
    if g.ccbox(msg,title):
        pass    # 如果用户选择Continue
    else:
        sys.exit(0)     # 如果用户选择Cancel'''

'''
# -*- coding: UTF-8 -*-
from easygui import *

# 定义一个叫做“Settings”的类，继承自EgStore
class Settings(EgStore):

    def __init__(self,filename): # 需要指定文件名
        # 指定要记住的属性名称
        self.author = ""
        self.book = ""

        # 必须执行下面两个语句
        self.filename = filename
        self.restore()

# 创建“Settings”的实例化对象”settings“
settingsFilename = 'settings.txt'
settings = Settings(settingsFilename)

author = "小甲鱼"
book = "零基础入门学习"

# 将上面两个变量的值保存到“settings”对象中
settings.author = author
settings.book = book
settings.store()
print("\n保存完毕\n")
f = open('settings.txt','rb')
nr = f.readlines()
print(nr)
f.close()
'''

# test 1
# from easygui import *
# import random
#
# while True:
#     num = random.randint(1, 10)
#
#     num2 = integerbox('猜猜我现在心中想的是哪个数字（1-10）', '猜数字小游戏', lowerbound=1, upperbound=10)
#     if num == num2:
#         re = ccbox('恭喜你猜对啦！还要继续吗？', '猜数字小游戏')
#     else:
#         re = ccbox('很遗憾，你猜错了，我想的是%d,还要继续吗？' % num, '猜数字小游戏')
#
#     if re:
#         pass
#     else:
#         msgbox('拜拜了您嘞！！！','游戏结束')
#         break

# test 2
# from easygui import *
#
# user = ['*用户名','*真实姓名','固定电话','*手机号码','QQ','*E-mail']
#
# while True:
#     user1 = multenterbox("【*真实姓名】为必填项\n【*手机号码】为必填项\n【*E-mail为必填项】","用户中心",user)
#     if (user1[0] == '') or (user1[1] == '')  or (user1[3] == '') or (user1[5] == ''):
#         msgbox("必填项不可为空！！！，请重新填写信息","用户中心")
#         continue
#     else:
#         for line in range(0,5):
#             if ' ' in user1[line]:
#                 msgbox('%s中存在空格,请重新填写信息' % user[line])
#                 break
#             else:
#                 textbox("信息录入完成，您的信息是：","用户中心",text=[user1[0],user1[1],user1[2],user1[3],user1[5]])
#                 break
#     continue

# test 3
# from easygui import *
# import os
#
# filepath = fileopenbox('请选择你要打开的文本文件','文件访问',default=r'C:\Users\12\Desktop\*.txt',filetypes='*.txt')
# filelist = filepath.split('\\')
# filename = filelist[-1]
# f = open(filepath,'r+',encoding='utf-8')
# nr = f.readlines()
# f.close()
# textbox('%s的内容是：' % filename,'文本显示',text=nr)

# test 4
# from easygui import *
#
# filepath = fileopenbox('请选择你要打开的文本文件','文件访问',default=r'C:\Users\12\Desktop\*.txt',filetypes='*.txt')
# filelist = filepath.split('\\')
# filename = filelist[-1]
# f = open(filepath,'r+',encoding='utf-8')
# text = f.readlines()
# f.close()
# text1 = textbox('%s的内容是：' % filename,'文本显示',text=text)
# text2 = ''
# for line in text:
#     text2 = text2 + line
#
# if text1 == None:
#     pass
# elif text1 != text2:
#     choices = ['覆盖保存', '放弃保存', '另存为...']
#     choice = buttonbox('监测到文本内容存在更改，请选择以下操作：','警告',choices=choices)
#     if choice == choices[0]:
#         f = open(filepath,'w',encoding='utf-8')
#         f.write(text1)
#         f.close()
#     elif choice == choices[1]:
#         f.close()
#         pass
#     else:
#         f.close()
#         userfile = filesavebox('请输入你要保存的文件名','文件保存',default=r'C:\Users\12\Desktop\1.txt',filetypes='*.txt')
#         f = open(userfile, 'w', encoding='utf-8')
#         f.write(text1)
#         f.close()
# else:
#     pass

'''

# test 5
import os
from easygui import *
import io

def read_line(filepath):
    # f = open(filepath,'r',encoding='utf-8')
    # file = f.readlines()
    # lines = len(file)
    try:
    # f.close()
    lines = 0
        with io.open(filepath,'r',encoding='utf-8') as f:
            file = f.readlines()
            lines = len(file)
        
    except:
        pass
    
    return lines

def search_file(path):
    # num1 = 0
    lines1 = 0
    list1 = [0,0]
    numlist = [0, 0]
    filelist = os.listdir(path)
    num = len(filelist)
    # print(filelist)
    for i in range(0,num):
        filepath = path + '\\' +filelist[i]
        if os.path.isdir(filepath):
            list1 = search_file(filepath)
            num2 = int(list1[0])
            lines2 = int(list1[1])
            numlist[0] = int(numlist[0]) + int(num2)
            numlist[1] = int(numlist[1])+ int(lines2)
            # print(numlist)
        else:
            name = filelist[i].split('.')
            name = name[-1]
            if name == 'py':
                line = read_line(filepath)
                # print(lines1)
                lines1 += line
                # print(lines1)
                numlist[0] = int(numlist[0]) + 1
                numlist[1] = int(numlist[1]) + int(lines1)
                lines1 = 0
                # print(numlist)

    return numlist

LibraryPath = diropenbox('请选择你的代码库文件夹：','库文件选择')
Statistics = search_file(LibraryPath)
# print(Statistics)
line = int(Statistics[1])
lines = integerbox('请输入你的目标源代码行数（最大为10000000000）',lowerbound=0,upperbound=10000000000)
bfb = ('{:.2%}'.format(line/lines))
text = ('您的目标是%d行\n\n您已编写了：\n\t%s个Python源文件\n\t%s行源代码\n\t已完成目标的%s' % (lines,Statistics[0],Statistics[1],bfb))
msgbox(text,'数据统计')
# print(Statistics)
'''

# list1 = ['1','211','123']
# aaa = "\n".join(list1)
# print(aaa)