from easygui import *
import os,time

name = enterbox('请输入你需要查找的文件名称','文件查找')

def search_file(filename,filepath1):
    list1 = []
    try:
        filelist = os.listdir(filepath1)
    except (PermissionError,FileNotFoundError):
        return 1
    num = len(filelist)
    # print(num)
    times = 1

    for i in range(0,num):
        filepath = filepath1 + '\\' +filelist[i]
        # print(filelist[i],filepath)
        name = filelist[i]
        # print(name)
        if filename in name:
            list1.append(filepath)

        else:
            if os.path.isdir(filepath):
                list2 = search_file(filename,filepath)
                if list2 == 1:
                    continue
                list1 = list1 + list2
                times += 1
            else:
                if filename in name:
                    list1.append(filepath)
                else:
                    times += 1
                    continue

    return list1
pathlist = ["C:\\","D:\\","E:\\","F:\\","G:\\"]
# path = ('C:\\')
print(time.ctime())
filelist = []
for path in pathlist:
    path = search_file(name,path)
    for line in path:
        # print(line)
        filelist.append(line)
# print(time.ctime())
# print(path)
text = "\n".join(filelist)
textbox('搜索结果如下：','文件搜索',text=text)