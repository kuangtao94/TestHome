# -*- coding: utf-8 -*-
# python 3.5.0
import time as t
from selenium import webdriver
def wait():
    t.sleep(5)
def login(driver,username = "123456",password = "123456" ):
    wait()
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[3]/a[7]").click()
    wait()
    driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
    wait()
    driver.username = username
    driver.find_element_by_id("TANGRAM__PSP_10__userName").send_key(driver.username)
    wait()
    driver.password = password
    driver.find_element_by_id("TANGRAM__PSP_10__password").send_key(driver.password)
    driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
