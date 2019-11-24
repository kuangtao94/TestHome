# coding:utf-8
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://192.168.0.112/ranzhi/www/sys/user-login.html")
driver.find_element_by_id("account").send_keys("yifeng")
driver.find_element_by_id("password").send_keys("yifeng123")
driver.find_element_by_id("submit").click()
sleep(1)
driver.find_element_by_xpath('//*[@id="s-menu-2"]/button/img').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="mainNavbar"]/ul/li[5]/a').click()

driver.switch_to_frame('iframe-2')
driver.find_element_by_xpath('//*[@id="menuActions"]/a[2]').click()
sleep(1)
driver.find_element_by_xpath('//*[@id="typesick"]').click()

driver.find_element_by_xpath('//*[@id="typesick"]').click()
driver.find_element_by_xpath('//*[@id="typesick"]').click()