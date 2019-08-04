#!/usr/bin/env python
#coding:utf-8

import unittest_1
from selenium import  webdriver

class Baidu(unittest_1.TestCase):
	def setUp(self):
		self.driver=webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
		self.driver.get('http://www.baidu.com')

	def tearDown(self):
		self.driver.quit()

	def test_baidu_title(self):
		'''验证百度首页的title'''
		self.assertEqual(self.driver.title,'百度一下，你就知道')

	def test_baidu_url(self):
		'''验证百度首页的URL'''
		self.assertEqual(self.driver.current_url,'https://www.baidu.com')

	def test_baidu_news(self):
		'''验证百度新闻的URL地址'''
		self.driver.find_element_by_link_text('新闻').click()
		url=self.driver.current_url
		self.assertEqual(self.driver.current_url,'https://www.baidu.news/')


if __name__ == '__main__':
    unittest_1.main(verbosity=2)
