#coding:utf-8
from selenium import webdriver
from time import sleep
import os
import unittest       #引入单元测试框架
from TestCase.auto_test_leke.web_test.src.common.method import public
from selenium.webdriver.common.by import By                  #导入by定位
from selenium.webdriver.support.ui import WebDriverWait   #导入显示等待包
from selenium.webdriver.support import expected_conditions as EC  #导入期望条件
import sys  #导入python自身的包
from TestCase.auto_test_leke.web_test.data.excel import excle_data
reload(sys)  #重载sys包
sys.setdefaultencoding("utf-8")  # 设置python默认编码为utf-8
class hetong(unittest.TestCase):
    def setUp(self):                #测试用例的初始化部分
        global driver,common        #声明全局变量
        driver=webdriver.Chrome()
        data=excle_data()              #创建excel数据类对象
        ge =data.get_sheet1(2)    #获取excel表中的第二行
        driver.get('http://192.168.0.111/ranzhi/www/sys/user-login.html')
        common=public(driver)       #创建公共类对象
        common.input_text(By.ID,'account',ge[0])
        common.input_text(By.ID,'password',ge[1])
        common.click_element(By.ID,'submit')
    def test_creat_hetong(self):    #真正的测试用例部分
        """测试新建合同"""
        common.click_element(By.XPATH,'//*[@id="mainNavbar"]/div/ul[2]/li[5]/a')
        # driver.find_element_by_xpath('//*[@id="mainNavbar"]/div/ul[2]/li[5]/a').click()      #点击合同
        sleep(1)
        driver.switch_to_frame('iframe-dashboard')
        common.click_element(By.XPATH,'//*[@id="menuActions"]/a')
        # driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()                     #点击新建合同
        sleep(1)
        driver.switch_to_default_content()
        driver.switch_to_frame('iframe-1')
        sleep(1)
        js='var q=document.getElementById("customer").style.display="block"'
        driver.execute_script(js)
        sleep(1)
        common.input_text(By.XPATH,'//*[@id="customer"]',u'养猪大户',0)
        # driver.find_element_by_xpath('//*[@id="customer"]').send_keys(u'养猪大户')        #客户名
        common.input_text(By.XPATH,'//*[@id="orderTD"]/div/span[1]/select',u'养猪大户购买葫芦娃',0)
        # driver.find_element_by_xpath('//*[@id="orderTD"]/div/span[1]/select').send_keys(u'养猪大户购买葫芦娃')
        common.click_element(By.XPATH,'//*[@id="begin"]')
        # driver.find_element_by_xpath('//*[@id="begin"]').click()
        common.click_element(By.XPATH,'/html/body/div[3]/div[3]/table/tbody/tr[5]/td[1]')
        # driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr[5]/td[1]').click()
        common.click_element(By.XPATH,'//*[@id="end"]')
        # driver.find_element_by_xpath('//*[@id="end"]').click()
        common.click_element(By.XPATH,'/html/body/div[4]/div[3]/table/tbody/tr[5]/td[2]')
        # driver.find_element_by_xpath('/html/body/div[4]/div[3]/table/tbody/tr[5]/td[2]').click()
        common.click_element(By.XPATH,'//*[@id="fileBox1"]/tbody/tr/td[1]/div/input')
        # driver.find_element_by_xpath('//*[@id="fileBox1"]/tbody/tr/td[1]/div/input').click()    #添加名称
        os.chdir(r'D:\python_work')               #切换到程序对应的文件夹下
        os.system('auto_it.exe')
        common.click_element(By.XPATH,'//*[@id="submit"]')
        # driver.find_element_by_xpath('//*[@id="submit"]').click()
    def tearDown(self):            #测试用例的退出部分
        sleep(1)
        driver.switch_to_default_content()
        common.click_element(By.XPATH,'//*[@id="start"]')
        common.click_element(By.XPATH,'//*[@id="startMenu"]/li[10]/a')






