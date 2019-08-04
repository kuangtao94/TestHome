#!/usr/bin/env python
#coding:utf-8 

#Author:无涯

from base.base import *
from selenium.webdriver.common.by import By

class Baidu(WebUi):
	so_loc=(By.ID,'kw')

	def typeSo(self,keyword):
		'''百度搜索输入框输入关键字'''
		self.findElement(*self.so_loc).send_keys(keyword)

	def getKeyword(self):
		'''返回输入的搜索关键字'''
		return self.findElement(*self.so_loc).get_attribute('value')

