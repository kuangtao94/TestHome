#coding:utf-8
from selenium import webdriver
from time import sleep
from TestCase.auto_test_leke.web_test.src.common.method import public
import os
from selenium.webdriver.common.by import By                  #导入by定位
from selenium.webdriver.support.ui import WebDriverWait   #导入显示等待包
from selenium.webdriver.support import expected_conditions as EC  #导入期望条件
driver=webdriver.Chrome()
# driver.get('http://192.168.0.111/ranzhi/www/sys/user-login.html')
driver.get('http://192.168.0.111/crm/index.php?m=user&a=login')
#显示等待作用：1、灵活等待，当元素被定位时，返回该元素
#2、在设置时间内找到元素，找不到报错
#3、浏览器对象    最大等待时间    刷新间隔
#当定位到期望条件的元素，停止等待     ,EC.presence_of_all_elements_located方法只能携带一个参数，以元组方式传入
# element = WebDriverWait(driver,5,0.5).until(EC.presence_of_all_elements_located((By.ID,"account")))
# element.send_keys('fu1234')
# # driver.find_element_by_id('account').send_keys('fu1234')
s=public(driver)
s.login('fu','fu123')
# driver.find_element_by_id('password').send_keys('fu1234')
# driver.find_element_by_id('submit').click()
#
#
#
# name=driver.find_element_by_xpath('//*[@id="mainNavbar"]/div/ul[1]/li/a').text
# print(name)
# sleep(2)
# driver.find_element_by_xpath('//*[@id="mainNavbar"]/div/ul[2]/li[3]/a').click()
#  切换到子框架中
# driver.switch_to_frame('iframe-dashboard')
#
# 切换回原页面框架中
# driver.switch_to_default_content()
#
#
# driver.find_element_by_xpath('//*[@id="createButton"]').click()
# driver.find_element_by_xpath('//*[@id="name"]').send_keys(u'划水')
#  js='var q=document.getElementById("manager").style.display="block"'
#  driver.execute_script(js)
# sleep(1)
#  driver.find_element_by_xpath('//*[@id="manager"]').send_keys(u'陈富华')
# driver.find_element_by_xpath('//*[@id="manager_chosen"]/a/').click()#send_keys(u'陈富华')
# driver.find_element_by_css_selector('li.active-result:nth-child(45)').click()
# id=driver.find_element_by_id('manager')
#  ren=id.find_elements_by_tag_name('li')
#  ren[6].click()
#
# sleep(1)
# driver.find_element_by_id('begin').send_keys('2018-10-20')
#  driver.find_element_by_xpath('//*[@id="begin"]').send_keys('2018-10-19')
# driver.find_element_by_xpath('/html/body/div[3]/div[3]/table/tbody/tr[4]/td[6]').click()
#
# sleep(1)
# driver.find_element_by_id('end').send_keys('2018-10-21')
# driver.find_element_by_xpath('/html/body/div[4]/div[3]/table/tbody/tr[4]/td[7]').click()
#
#  driver.find_element_by_xpath('//*[@id="end"]').send_keys('2018-10-19')
# sleep(1)
#  driver.switch_to_frame('ke-edit-iframe')
# driver.find_element_by_css_selector('body').send_keys(u'逃跑计划')
# sleep(2)
# driver.find_element_by_xpath('//*[@id="whitelist1"]').click()
# driver.find_element_by_xpath('//*[@id="submit"]').click()




