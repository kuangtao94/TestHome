#coding:utf-8
from selenium import webdriver
from time import sleep
import time
import unittest       #引入单元测试框架
from TestCase.auto_test_leke.web_test.src.common.method import public
from selenium.webdriver.common.by import By                  #导入by定位
from TestCase.auto_test_leke.web_test.config import param
from TestCase.auto_test_leke.web_test.data.excel import excle_data
from random import Random

import sys  #导入python自身的包
reload(sys)  #重载sys包
sys.setdefaultencoding("utf-8")  # 设置python默认编码为utf-8
class xiansuo(unittest.TestCase):
    def setUp(self):
        global driver,common,ge,num
        driver=webdriver.Chrome()
        common=public(driver)
        driver.get('http://192.168.0.111/crm/index.php?m=user&a=login')
        common.login('fu','fu123')
    def test_xiansuo(self):
        common.click_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a')
        # driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a').click() #点击线索
        common.click_element(By.XPATH,'/html/body/div[5]/div[2]/div[1]/div/a')
        # driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div/a').click()          #点击新建线索
        common.click_element(By.XPATH,'//*[@id="owner_name"]')
        # driver.find_element_by_xpath('//*[@id="owner_name"]').click()                          #点击负责人框
        common.click_element(By.XPATH,'//*[@id="d_content"]/tr[18]/td[1]')
        # driver.find_element_by_xpath('//*[@id="d_content"]/tr[18]/td[1]').click()              #选择负责人
        common.click_element(By.XPATH,'/html/body/div[7]/div[3]/div/button[1]/span')
        # driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/button[1]/span').click()    #点击ok
        common.input_text(By.XPATH,'//*[@id="name"]',ge[num])
        # driver.find_element_by_xpath('//*[@id="name"]').send_keys(u'学校')
        # driver.find_element_by_xpath('//*[@id="source"]/option[4]').click()   #点击下拉框的某一项进行选择
        common.input_text(By.XPATH,'//*[@id="source"]',u'合作伙伴',0)
        # driver.find_element_by_xpath('//*[@id="source"]').send_keys(u'合作伙伴')  #已输入的方式选择下拉框中的选项
        common.input_text(By.XPATH,'//*[@id="contacts_name"]',u'陈二')
        # driver.find_element_by_xpath('//*[@id="contacts_name"]').send_keys(u'陈二')
        common.input_text(By.XPATH,'//*[@id="nextstep_time"]','2018-10-19 14:17')
        # driver.find_element_by_xpath('//*[@id="nextstep_time"]').send_keys('2018-10-19 14:17')
        common.click_element(By.XPATH,'//*[@id="form1"]/table/tfoot/tr/td/input[2]')
        # driver.find_element_by_xpath('//*[@id="form1"]/table/tfoot/tr/td/input[2]').click()    #点击保存新建线索
        sleep(1)
        name=common.locat_element(By.XPATH,'//*[@id="form1"]/table/tbody/tr[1]/td[3]/a').text
        #断言
        self.assertEqual(name,ge[num])
        #当前系统时间
        now=time.strftime('%y-%m-%d_%H-%M-%S',time.localtime())
        #截图
        driver.get_screenshot_as_file(param.img_path+now+".png")
def tearDown(self):            #测试用例的退出部分
        common.click_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a')
        common.click_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/ul/li[12]/a')