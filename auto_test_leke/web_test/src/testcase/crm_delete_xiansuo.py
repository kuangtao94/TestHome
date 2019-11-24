#coding:utf-8
from selenium import webdriver
from time import sleep
import time
import unittest       #引入单元测试框架
from TestCase.auto_test_leke.web_test.src.common.method import public
from selenium.webdriver.common.by import By                  #导入by定位
from selenium.webdriver.support.ui import WebDriverWait   #导入显示等待包
from selenium.webdriver.support import expected_conditions as EC  #导入期望条件
import sys  #导入python自身的包
reload(sys)  #重载sys包
sys.setdefaultencoding("utf-8")  # 设置python默认编码为utf-8

class delete(unittest.TestCase):
    def setUp(self):
        global del1,delete
        delete=webdriver.Chrome()
        del1=public(delete)
        delete.get('http://192.168.0.111/crm/index.php?m=user&a=login')
        del1.login('fu','fu123')
        # delete.find_element_by_name('name').send_keys('fu')
        # delete.find_element_by_name('password').send_keys('fu123')
        # delete.find_element_by_name('submit').click()
    def test_creat_hetong(self):
        del1.click_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a')
        # delete.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/ul[1]/li[1]/a').click()  #点击线索
        del1.click_element(By.XPATH,'//*[@id="form1"]/table/tbody/tr[15]/td[1]/input')
        # delete.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr[15]/td[1]/input').click()
        del1.click_element(By.XPATH,'//*[@id="form1"]/table/tbody/tr[2]/td[1]/input')
        del1.click_element(By.XPATH,'/html/body/div[5]/div[2]/div[1]/ul/li[1]/div/a')
        # delete.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/ul/li[1]/div/a').click()
        del1.click_element(By.XPATH,'//*[@id="delete"]')
        # delete.find_element_by_xpath('//*[@id="delete"]').click()
        delete.switch_to_alert().accept()
    def tearDown(self):
        del1.click_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/a')
        del1.click_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/ul[2]/li[6]/ul/li[12]/a')

# name=delete.find_element_by_xpath('/html/body/div[5]/div[3]/div[1]/div/div[1]/div[2]/p[1]').text   #获取屏幕文本
# now=time.strftime('%y-%m-%d_%H-%M-%S',time.localtime())        #获取系统时间并转化成字符串
# delete.get_screenshot_as_file(r"D:\python_work\auto_test\img\login"+now+".png")             #获取屏幕截图
# delete.find_element_by_xpath('').click('//*[@id="delete"]')

#通过js语句控制滚动条   控制滚动条与页面顶端的距离
# js='document.documentElement.scrolltop=100'
# sleep(2)
# delete.execute_script(js)             #执行定义好的js语句

#点击列表最后一个

#处理警告框
# delete.switch_to_alert().accept()    #相当于在警告框中点击确定
# delete.switch_to_alert().dismiss()   #相当于在警告框中点击取消
# text=delete.switch_to_alert().text   #获取警告框中中的文字