import xlrd2
import os

'''
xlrd的2.0.1版本不支持xlsx格式的文档，需要卸载后下载1.2.0版本
os.path.join拼接可能会出现双斜杠的问题，可以通过replace方法替换
'''

def dir_name():
    return os.path.dirname(__file__)

def read_excal(name):
    lists = []
    dir_path = os.path.join(dir_name(),name)
    dir_path = dir_path.replace('\\','/')
    value = xlrd2.open_workbook(dir_path)
    book = value.sheet_by_index(0)  # 通过索引定位到Excel表格的第一张
    for item in range(1, book.nrows):   # 因为第一行是属性，所以不使用，从索引1开始循环第一张的所有单元格
        lists.append(book.row_values(item)) # 返回切片单元格的值添加到列表lists中

    return lists
    # print(lists)

# if __name__ == '__main__':
#     read_excal('data.xlsx')