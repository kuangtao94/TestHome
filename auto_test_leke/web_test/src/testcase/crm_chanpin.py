# coding:utf-8
from selenium import webdriver
from time import sleep
import os       #导入系统包
from TestCase.auto_test_leke.web_test.src.common.method import public
from selenium.webdriver.common.by import By                  #导入by定位
import time
import unittest
import sys  #导入python自身的包
from TestCase.auto_test_leke.web_test.data.excel import excle_data
from TestCase.auto_test_leke.web_test.config import param
from TestCase.auto_test_leke.web_test.data.excel import excle_data
from random import Random
Random.reload(sys)  #重载sys包
sys.setdefaultencoding("utf-8")  # 设置python默认编码为utf-8
class chanpin(unittest.TestCase):
    def setUp(self):
        global s,common,ge,num
        s=webdriver.Chrome()
        common=public(s)
        data=excle_data()
        ge=data.get_sheet2(2)
        ran=Random()
        num=ran.randint(1,14)
        s.get('http://192.168.0.111/crm/index.php?m=user&a=login')
        common.login('fu','fu123')
        # s.find_element_by_name('name').send_keys('fu')
        # s.find_element_by_name('password').send_keys('fu123')
        # s.find_element_by_name('submit').click()
    def test_chanpin(self):    #真正的测试用例部分
        common.click_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[1]/li[4]/a')
        # s.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[4]/a').click()
        common.click_element(By.XPATH,'/html/body/div[5]/div[2]/div[2]/div[2]/a')
        # s.find_element_by_xpath('/html/body/div[5]/div[2]/div[2]/div[2]/a').click()
        common.input_text(By.XPATH,'//*[@id="name"]',ge[num])
        # s.find_element_by_xpath('//*[@id="name"]').send_keys(u'胡歌')
        common.input_text(By.XPATH,'//*[@id="development_team"]',u'胡歌')
        # s.find_element_by_xpath('//*[@id="development_team"]').send_keys(u'胡歌')
        common.click_element(By.XPATH,'//*[@id="form1"]/table/tbody/tr[7]/td[2]/table/tbody/tr/td[4]/div')
        # s.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[7]/td[2]/table/tbody/tr/td[4]/div').click()
        sleep(1)
        os.chdir(param.d_path)               #切换到程序对应的文件夹下
        os.system('auto_it.exe')
        # s.find_element_by_xpath('//*[@id="main_pic"]').click()
        # s.find_element_by_xpath('//*[@id="main_pic"]').send_keys(r'D:\python_work\auto_test\img\login18-10-22_09-44-48.png')
        common.click_element(By.XPATH,'//*[@id="form1"]/table/tfoot/tr/td/input[1]')
        # name=common.locat_element(By.XPATH,'//*[@id="form1"]/table/tbody/tr[1]/td[5]/a').text
        # self.assertEqual(name,'fu')
        sleep(1)
        name=common.locat_element(By.XPATH,'//*[@id="form1"]/table/tbody/tr[1]/td[3]/a').text
        self.assertEqual(name,ge[num])
        now=time.strftime('%y-%m-%d_%H-%M-%S',time.localtime())
        #截图
        s.get_screenshot_as_file(param.img_path+now+".png")
        # s.find_element_by_xpath('//*[@id="form1"]/table/tfoot/tr/td/input[2]').click()
    def tearDown(self):            #测试用例的退出部分
        common.click_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a')
        common.click_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/ul/li[12]/a')