# -*- coding: UTF-8 -*-
import xlrd2
import os
import xlwt

'''
xlrd的2.0.1版本不支持xlsx格式的文档，需要卸载后下载1.2.0版本
os.path.join拼接可能会出现双斜杠的问题，可以通过replace方法替换
'''

def dir_name():
    return os.path.dirname(__file__)

def read_excal(name):
    lists = []
    dir_path = os.path.join(dir_name(), name)
    dir_path = dir_path.replace('\\', '/')
    value = xlrd2.open_workbook(dir_path)
    book = value.sheet_by_index(0)  # 通过索引定位到Excel表格的第一张

    wb = xlwt.Workbook(encoding='utf-8')  # 新建一个excel文件
    ws1 = wb.add_sheet('first')  # 添加一个新表，名字为first
    a = 0   # 行数初始化
    for item in range(1, book.nrows):  # 因为第一行是属性，所以不使用，从索引1开始循环第一张的所有单元格
        functions = ('功能点：%s-%s-%s-%s' % (
        book.row_values(item)[0], book.row_values(item)[1], book.row_values(item)[2], book.row_values(item)[3]))
        txt = ('%s\n步骤\n%s\n预期结果\n%s' % (functions, book.row_values(item)[6], book.row_values(item)[7]))
        ws1.write(a, 0, txt)
        # a为行数，0为列数
        a += 1
    wb.save('111.xls')  # 保存excal文件

lists = read_excal('Viva.xlsx')