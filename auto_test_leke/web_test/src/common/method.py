# coding:utf-8
from selenium import webdriver
import os
from selenium.webdriver.common.by import By                  #导入by定位
from selenium.webdriver.support.ui import WebDriverWait   #导入显示等待包
from selenium.webdriver.support import expected_conditions as EC  #导入期望条件
from logging import log                                                #导入日志文件中的日志 类

# driver=webdriver.Chrome()
class public():
    def __init__(self,driver):           #创建对象时加入初始化参数,每次调用类时都会执行初始化参数
        self.driver=driver
        self.log=log('execute.log')                 #创建日志类对象，并初始化文件
    def login(self,username,password):
        self.input_text(By.NAME,"name",username)
        self.input_text(By.NAME,"password",password)
        self.click_element(By.NAME,"submit")
    def logout(self):
        self.click_element(By.XPATH,'')
    def locat_element(self,*loc):    #定义元素的方法
        try:
            element = WebDriverWait(self.driver,5,0.5).until(
                    EC.presence_of_element_located(loc)
            )
            return element
        except:
            self.log.error(u"元素找不到"+str(loc))
    def input_text(self,a,b,text,clear=True):         #输入框的方法
        if clear:
            try:
                self.locat_element(a,b).clear()
                self.locat_element(a,b).send_keys(text)
            except:
                self.log.error(u'文本输入失败'+str(text))
        else:
            try:
                self.locat_element(a,b).send_keys(text)
            except:
                self.log.error(u'文本输入失败'+str(text))
    def click_element(self,a,b):               #点击元素的方法
        try:
            self.locat_element(a,b).click()
        except:
                self.log.error(u'点击失败'+str(b))
