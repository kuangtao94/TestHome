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
        global driver,common,num,ge
        driver=webdriver.Chrome()
        common=public(driver)
        data=excle_data()
        ge=data.get_sheet2(2)
        ran=Random()
        num=ran.randint(1,14)
        driver.get('http://192.168.0.111/crm/index.php?m=user&a=login')
        common.login('fu','fu123')
    def test_shangji(self):
        common.click_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[1]/li[5]/a')
        common.click_element(By.XPATH,'/html/body/div[5]/div[2]/div[1]/div/a')
        common.input_text(By.XPATH,'//*[@id="subject"]',ge[num])
        common.click_element(By.XPATH,'//*[@id="owner_name"]')
        common.click_element(By.XPATH,'//*[@id="ta1"]/span[41]/input')
        common.click_element(By.XPATH,'/html/body/div[7]/div[3]/div/button[1]')
        common.click_element(By.XPATH,'/html/body/div[5]/div[2]/div/form/table/tfoot/tr/td[2]/input[1]')
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
        driver.close()