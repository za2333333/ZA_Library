# -*- coding: UTF-8 -*-
import asyncio
import re
import os
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import aiohttp
import aiofiles

# 登录模块
def login():
    driver = webdriver.Chrome()
    global drver
    url = 'https://user.qzone.qq.com/1083554260/4'
    driver.get(url)
    sleep(20)
    xf = driver.find_element(by=By.XPATH,value='//*[@id="login_frame"]')
    driver.switch_to.frame(xf)
    driver.find_element(by=By.XPATH,value='//*[@id="img_out_1083554260"]').click()
    sleep(10)
    return driver

# 获取cookie
def get_cookie(driver):
    cookies = driver.get_cookies()
    cookielist = [cookie['name'] + '=' + cookie['value'] for cookie in cookies]
    cookiestr = ';'.join(cookielist)
    return cookiestr

# 获取动态加载后的空间相册代码
def get_page(driver):
    # driver = login()
    driver.set_window_size(480, 800)
    js = "window.scrollTo(0,document.body.scrollHeight)"
    driver.execute_script(js)
    sleep(5)
    f1 = driver.find_element(by=By.XPATH,value='//*[@id="tphoto"]')
    driver.switch_to.frame(f1)
    sleep(1)
    page = driver.page_source
    return page

# 获取所有相册信息
def get_album_list(page):
    page_text = BeautifulSoup(page,"html.parser")
    album_list = page_text.find_all('div',class_="bg bor3 mod-album js-album-item js-album-transition")
    list1 = []
    for albums in album_list:
        id = albums.get('data-id')
        name = albums.get('data-name')
        num = albums.get('data-total')
        datalist = []
        if (int(num) > 400):
            datalist.append(id)
            datalist.append(name)
            datalist.append(400)
            list1.append(datalist)
            datalist = []
            num = int(num) - 400
        datalist.append(id)
        datalist.append(name)
        datalist.append(num)
        list1.append(datalist)
    return list1

# 处理URL中的必要信息
def get_g_tk(driver):
    g_tk = driver.execute_script('return QZONE.FP.getACSRFToken()')
    return g_tk

# 处理所有相册的URL
def get_url(lists,g_tk):
    urllist = []
    olddata = [0]
    for data in lists:
        if (data[0]==olddata[0]):
            url = ("https://h5.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/cgi_list_photo?g_tk=%s&callback=shine0_Callback&t=826272405&mode=0&idcNum=4&hostUin=1083554260&topicId=%s&noTopic=0&uin=1083554260&pageStart=400&pageNum=%d&skipCmtCount=0&singleurl=1&batchId=&notice=0&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone&plat=qzone&outstyle=json&format=jsonp&json_esc=1&question=&answer=&callbackFun=shine0&_=1668081263010" % (g_tk,data[0],int(data[2])))
        else:
            url = ("https://h5.qzone.qq.com/proxy/domain/photo.qzone.qq.com/fcgi-bin/cgi_list_photo?g_tk=%s&callback=shine0_Callback&t=826272405&mode=0&idcNum=4&hostUin=1083554260&topicId=%s&noTopic=0&uin=1083554260&pageStart=0&pageNum=%d&skipCmtCount=0&singleurl=1&batchId=&notice=0&appid=4&inCharset=utf-8&outCharset=utf-8&source=qzone&plat=qzone&outstyle=json&format=jsonp&json_esc=1&question=&answer=&callbackFun=shine0&_=1668081263010" % (g_tk,data[0],int(data[2])))
        urllist.append(url)
        olddata = data
    return urllist

# 将所有相册信息写入文件中
async def write_url(url,headers,list1,session):
    async with session.get(url,headers=headers,verify_ssl=False) as resp:
        async with aiofiles.open(f'./data/{list1[1]}data.txt',mode='a+') as f:
            page = await resp.text()
            obj = re.compile(r'"lloc" : "(?P<lloc>.*?)".*?'
                             r'"name" : "(?P<name>.*?)".*?'
                             r'"raw" : "(?P<url>.*?)",.*?'
                             r'"rawshoottime" : "(?P<time>.*?)",.*?'
                             r'"url" : "(?P<url1>.*?)",', re.S)
            photodata_list = obj.finditer(page)
            for photo in photodata_list:
                if photo.group('url') == '':
                    photourl = photo.group('url1')
                else:
                    photourl = photo.group('url')
                photoname = photo.group('time').replace(' ','-').replace(':','-')
                photo = ("%s %s %s\n"%(photoname,photourl,list1[1]))
                await f.write(photo)


# 请求所有相册的信息
async def get_photo(urllist,headers,list1):
    task = []
    async with aiohttp.ClientSession() as session:
        i=0
        for url in urllist:
            task.append(asyncio.create_task(write_url(url,headers,list1[i],session)))
            i+=1
        await asyncio.wait(task)

# 下载照片并保存
async def download_photos(photolist,session):
    async with session.get(url = photolist[1],verify_ssl=False) as resp:
        if not (os.path.exists(f'./photo/{photolist[2]}/')):
            os.mkdir(f'./photo/{photolist[2]}/')
        async with aiofiles.open(f'./photo/{photolist[2]}/{photolist[0]}',mode='xb') as f:
            await f.write(await resp.content.read())

# 提取照片信息
async def get_photodata():
    dirlist = os.listdir('./data/')
    photoslist = []
    for dirone in dirlist:
        if ('.txt' not in dirone):
            continue
        with open(f'./data/{dirone}', mode='r', encoding='utf-8') as f:
            photolist = []
            num = 1
            for line in f.readlines():
                linelist = line.split(' ')
                photoname = ('%s-%d.png' % (linelist[0], num))
                num += 1
                photolist.extend([photoname.strip(), linelist[1], linelist[2].strip()])
                photoslist.append(photolist)
                photolist = []
    task = []
    async with aiohttp.ClientSession() as session:
        for each in photoslist:
            task.append(asyncio.create_task(download_photos(each,session)))
        await asyncio.wait(task)

def main():
    # 登录相册页面，传参
    driver = login()
    # 获取相册页面动态加载之后的页面代码
    page = get_page(driver)
    # 获取cookie
    cookies = get_cookie(driver)
    # 获取URL中的必要参数
    g_tk = get_g_tk(driver)
    # 从页面代码中提取相册的信息
    list1 = get_album_list(page)
    # 提取所有相册的URL
    urllist = get_url(list1,g_tk)
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "cookie": cookies
    }
    # 获取各个相册网页的源代码，提取所有照片的信息
    asyncio.run(get_photo(urllist,headers,list1))
    # 获取所有照片信息分析并下载写入
    asyncio.run(get_photodata())

if __name__ == "__main__":
    main()