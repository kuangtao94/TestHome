# coding:utf-8
from selenium import webdriver
from time import sleep
from TestCase.auto_test_leke.web_test.data.excel import excle_data
from random import Random
ran=Random()             #创建随机数的对象
num=ran.randint(1,3)
data=excle_data()
ge=data.get_sheet2(num)
driver = webdriver.Chrome()
driver.get("http://192.168.0.112/ranzhi/www/sys/user-login.html")
driver.find_element_by_id("account").send_keys("yifeng")
driver.find_element_by_id("password").send_keys("yifeng123")
driver.find_element_by_id("submit").click()
sleep(1)
driver.find_element_by_xpath('//*[@id="mainNavbar"]/div/ul[2]/li[4]/a').click() #点击订单
driver.switch_to_frame("iframe-dashboard")  #切换到子框架中
driver.find_element_by_xpath('//*[@id="menuActions"]/a').click() #创建订单
driver.switch_to_default_content()  # 切换回原页面
driver.switch_to_frame("iframe-1")  #切换到子框架中
driver.find_element_by_xpath('//*[@id="createCustomer"]').click()
driver.find_element_by_xpath('//*[@id="name"]').send_keys(ge[0])
driver.find_element_by_xpath('//*[@id="contact"]').send_keys("qiqi")
driver.find_element_by_xpath('//*[@id="phone"]').send_keys("17665270000")
sleep(1)
driver.find_element_by_xpath('//*[@id="createProduct"]').click()
driver.find_element_by_xpath('//*[@id="productName"]').send_keys(u"发布会")
driver.find_element_by_xpath('//*[@id="code"]').send_keys('sdsdf')
driver.find_element_by_xpath('//*[@id="type"]').send_keys(u"实体类")
driver.find_element_by_xpath('//*[@id="currency"]').send_keys(u"人民币")
driver.find_element_by_xpath('//*[@id="plan"]').send_keys("20000")
driver.find_element_by_xpath('//*[@id="submit"]').click()