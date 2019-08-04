#!/usr/bin/env python 
#-*-coding:utf-8-*-

#author:wuya


import  unittest_1
import  time as t
from appium import  webdriver
from page.singApp import SinaLogin
import  warnings



class SingAppTest(unittest_1.TestCase, SinaLogin):
	def setUp(self):
		warnings.simplefilter('ignore', ResourceWarning)
		desired_caps={}
		desired_caps['platformName']='Android'
		desired_caps['platformVersion']='6.0'
		desired_caps['deviceName']='meizu_M5'
		desired_caps['appPackage']='com.sina.mail'
		desired_caps['appActivity']='com.sina.mail.SplashActivity'
		desired_caps['unicodeKeyboard']=True
		desired_caps['resetKeyboard']=True
		self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

	def test_001(self):
		'''测试新浪邮箱APP登录成功'''
		self.login('wuya1303@sina.com','admin123')
		self.clickMenu
		nick=self.getNick
		self.exit()
		self.assertEqual(nick,'wuya1303@sina.com')

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
    unittest_1.main(verbosity=2)

