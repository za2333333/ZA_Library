# -*- coding: UTF-8 -*-
import os,os.path
import shutil

def cret_dir(path):
    if (os.path.exists(path)):
        shutil.rmtree(path) # 先删除，在创建

    os.mkdir(path)

def del_dir(path):
    if (os.path.exists(path)):
        shutil.rmtree(path)

def photo_path():
    path = os.getcwd() + '/photo'
    return path