"""
from baiduHq import webdriver,login
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
#参数数字为像素点
print("设置浏览器的宽480、高800显示")
driver.set_window_size(480,800)
driver.maximize_window()
login(driver)
driver.quit

from selenium import webdriver
import  time
driver = webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.get("http://www.youdao.com")
driver.maximize_window()
print("当前URL：",driver.current_url)
print("当前源码为："+ driver.page_source)
print("当前title标题"+driver.title)
driver.back() #浏览器返回操作
driver.find_element_by_link_text("新闻").click()
driver.refresh() #浏览器刷新操作
print("当前URL：",driver.current_url)
driver.forward() #浏览器前进操作
print("当前URL：",driver.current_url)
print("当前源码为："+ driver.page_source)
print("当前浏览器为："+driver.name)

driver.quit()

from selenium import webdriver
import time as t
driver = webdriver.Firefox()
driver.maximize_window()
driver.get("Http://www.baidu.com")
t.sleep(5)
driver.find_element_by_link_text("登录").click()
#获取当前窗口的句柄
ifame = driver.find_element_by_id("TANGRAM_PSP_3_from")
driver.switch_to_frame(ifame)
nowHandle = driver.current_window_handle
driver.find_element_by_class_name("pass-reglink pass-link").click()
#获取所有窗口的句柄
handles = driver.window_handles
for handle in handles:
    if handle != nowHandle:
        driver.switch_to_window(handle)
        print("我跳转了注册页面")
        driver.find_element_by_id("TANGRAM_PSP_3_userName").send_keys("18791851232")
        t.sleep(5)
        driver.close()
driver.switch_to_window(nowHandle)
print("我跳转到登录页面")
driver.find_element_by_id("TANGRAM_PSP_8_userName").send_keys("18791851232")
t.sleep(5)
driver.quit()
"""
"""
import urllib.request
respone = urllib.request.urlopen("http://www.fishc.com")
html = respone.read()
html1 = html.decode("utf-8")
print(html1)

URl爬虫入门
import urllib.request
req = urllib.request.urlopen("http://placekitten.com/g/200/300")
respone = urllib.request.urlopen(req)
cat_img = respone.read()
with open("cat_200_300.jpg","wb") as f:
    f.write(cat_img)

    #Python编写99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print("%s * %s = %s" % (i,j,i*j ),end=" ")
    print( )

    #使用有道进行翻译文本
import urllib.request
import urllib.parse
import json

content = input("请输入要翻译的内容：")
url = "http://fanyi.youdao.com/translate?smartresult = dict&smartresult = rule&smarttresult = ugc&sessionFrom = http://www.youdao.com/"
head = {}
head["Referer"] = "http://fanyi.youdao.com/"
head["User - Agent"] = "Moziila/5.0(Macintosh; Inter Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36X - Requested - With:XMLHttpRequest"
data = {}
data["type"] = "AUTO"
data["i"] = content
data["doctype"] = "json"
data["xmlVersion"] = "1.6"
data["keyfrom"] = "fanyi.web"
data["ue"] = "UTF - 8"
data["typeResult"] = "true"
data = urllib.parse.urlencode(data).encode("utf - 8")
req = urllib.request.Request(url,data,head)
respone = urllib.request.urlopen(req)
html = respone.read().decode("utf - 8")
target = json.loads(html)
print("翻译结果：%s " %(target["translateResult"][0][0]["tgt"]))

#使用代理的步骤如下：

import urllib.request

url = "http://www.whatismyip.com.tw"
proxy_support = urllib.request.ProxyHandler({"http":"211.138.121.38:80"})
#接着创建一个包含代理IP的opener
opener = urllib.request.build_opener(proxy_support)
#安装进默认环境
urllib.request.install_opener(opener)
#试试看IP地址修改了没
response = urllib.request.urlopen(url)
html = response.read().decode("utf - 8")
print(html)


#使用iplist进行填写多个IP地址
import urllib.request
import random

url = "http://www.whatismyip.com.tw"
print("添加代理模块IP地址(IP:端口号)，多个IP地址间用英文的分号隔开")
iplist = input("请输入IP地址：").split(sep = ";")
while  True:
    ip = random.choice(iplist)
    proxy_support = urllib.request.ProxyHandler({"http": "ip"})
    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [("User - Agent","Moziila/5.0(Macintosh; Inter Mac OS X 10_10_1) AppleWebKit/537.36(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36X - Requested - With:XMLHttpRequest")]
    urllib.request.install_opener(opener)
    try:
        print("正在尝试使用 %S 访问..."% ip )
        response = urllib.request.urlopen(url)
    except urllib.error.URLError:
        print("出错误了")
    else:
        print("访问成功！")
    if input("请问是否继续?(Y/N)") == "N":
        break

# Beautiful Soup 是一个可以从HTML 或 XML 文件文件中提取数据的Python库
# 设计出用户输入搜索关键词，按关键词进行检索出标题
import urllib.request
import urllib.parse
import re
from bs4 import BeautifulSoup

def main():
    keyword = input("请输入关键词：")
    keyword = urllib.parse.urlencode({"word" : keyword})
    response = \
urllib.request.urlopen("http://baike.baidu.com/search/word?%s"%keyword)
    html = response.read()
    soup = BeautifulSoup(html,"html.parser")

    for each in soup.find_all(href = re.compile("view")):
        content = "".join([each.text])
        url2 = "".join(["http://baike.baidu.com/",each["href"]])
        response2 = urllib.request.urlopen(url2)
        html2 = response.read()
        soup2 = BeautifulSoup(html2,"html.parser")
        if soup2.h2:
            content = "".join([content,soup2.h2.text])
        content = "".join([content,"->",url2])
        print(content)
if __name__ == "__main__":
    main()    


"""
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# import time
# driver = webdriver.Firefox()
# driver.get("http://www.baidu.com")
# #隐性等待30S
# driver.implicitly_wait(30)
# driver.get_screenshot_as_base64("F:/baidu.png")
# driver.quit()

#测试os.path路径
def url():
    print("XXurl首页地址")
def login():
    print("登录")
def logout():
    print("退出")

# str = "Teacher"
# class Person(object):
#     def __init__(self):
#         pass
#     def info(self):
#         print("调用Info方法")

# import login
# login.login()
import os,sys

for item in sys.path:
    print (item)


