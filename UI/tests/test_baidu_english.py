#!/usr/bin/env python
#coding:utf-8

#Author:无涯

import  unittest_1
from selenium import  webdriver
from page.baidu import Baidu
import  time
from page.init import  *

class BaiduTest(Init,Baidu):
	def test_baidu_so(self):
		self.typeSo('wuya')
		time.sleep(6)

if __name__ == '__main__':
    unittest_1.main(verbosity=2)