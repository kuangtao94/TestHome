#!/usr/bin/env python
#coding:utf-8 

#Author:无涯

import  unittest_1
from page.baidu import Baidu
from page.init import  Init


class BaiduTest(Init,Baidu):

	def test_baidu_so(self):
		'''测试:获取搜索的关键字并且验证它'''
		self.typeSo('无涯')
		self.assertEqual(self.getKeyword(),'无涯')

if __name__ == '__main__':
    unittest_1.main(verbosity=2)