# coding:utf-8
import requests                #可以使用代码发送http请求
import json                    #用来处理json数据
import unittest
from TestCase.auto_test_leke.interface_test.interface.interfacejb import interface   #导入封装好的接口类
class login(unittest.TestCase):
    def setUp(self):
        print('测试登录接口开始')
        global inter
        inter=interface()
    def test_login_1(self):
        """这是测试接口正例"""
        test=inter.login(13000000000,123456)
        self.assertEqual(test['message'],'success')
    def test_login_2(self):
        """这是登录接口：密码错误"""
        test=inter.login(13000000000,1234)
        self.assertEqual(test['message'],'password is error')
    def test_login_3(self):
        """这是登录接口：用户名错误"""
        test=inter.login(1300000000,123456)
        self.assertEqual(test['message'],'user is error')
    def tearDown(self):
        print('登录接口测试结束')