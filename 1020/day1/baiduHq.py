# -*- coding: utf-8 -*-
# python 3.5.0
import time as t
from selenium import webdriver
def wait():
    t.sleep(5)
def login(driver,username = "123456",password = "123456" ):
    wait()
    driver.find_element_by_id("ul").find_element_by_class_name("1b").click()
    wait()
    driver.find_element_by_id("TANGRAM__PSP_10__userName").send_key(username)
    wait()
    driver.find_element_by_id("TANGRAM__PSP_10__password").send_key(password)
    driver.find_element_by_id("TANGRAM__PSP_10__submit").click()
