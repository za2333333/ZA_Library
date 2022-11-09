import os
import csv

def dir_name():
    return os.path.dirname(__file__)

def read_csv(name):
    lists = []

    # 以字典的形式读写
    # with open(os.path.join(dir_name(),name),encoding='utf-8-sig') as f:
    with open(os.path.join(dir_name(), name),encoding='gbk') as f:
        value = csv.DictReader(f)   # 以字典的形式读取
        for i in value:
            lists.append(dict(i))

        # print(lists,type(lists[0]))
    return lists

    # # 以列表的形式读写
    # with open(os.path.join(dir_name(), name)) as f:
    #     value = csv.reader(f) # reader = csv.reader(f) 此时reader返回的值是csv文件中每行的列表，将每行读取的值作为列表返回
    #     # print(value)
    #     next(value)
    #     # # print(value)
    #     for i in value:
    #         # lists.append(dict(i))
    #         print(i)
    #
    #     # print(lists,type(lists[0]))

# if __name__ == '__main__':
#     read_csv('data.csv')