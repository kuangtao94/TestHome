import time as t
import warnings
from appium import webdriver
from UI.page.singApp import SinaLogin
import unittest_1
#
# class SinaAppTest(unittest_1.TestCase,SinaLogin):
#     def setUp(self):
#         warnings.simplefilter("ignore",ResourceWarning)
#         desired_caps={}
#         desired_caps["platformName"] = "Android"
#         desired_caps["platformVersion"] = "8.1.0"
#         desired_caps["deviceName"] = "4871660c"
#         desired_caps["appPackage"] = "com.sina.mail.free"
#         desired_caps["appActivity"] = "com.sina.mail.controller.FreeEntryActivity"
#         desired_caps["unicodekeyboard"] = True
#         desired_caps["resecodekeyboard"] = True
#         self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)
#
#
#
# if __name__ == '__main__':



warnings.simplefilter("ignore",ResourceWarning)
desired_caps={}
desired_caps["platformName"] = "Android"
desired_caps["platformVersion"] = "8.1.0"
desired_caps["deviceName"] = "4871660c"
desired_caps["appPackage"] = "com.sina.mail.free"
desired_caps["appActivity"] = "com.sina.mail.controller.FreeEntryActivity"
desired_caps["unicodekeyboard"] = True
desired_caps["resecodekeyboard"] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

driver.network_connection()
driver.set_network_connection(4)
driver.available_ime_engines()
driver.set_location()