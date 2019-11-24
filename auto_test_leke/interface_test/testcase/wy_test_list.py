# coding:utf-8
import requests                #可以使用代码发送http请求
import json                    #用来处理json数据
import unittest
from TestCase.auto_test_leke.interface_test.interface.interfacejb import interface   #导入封装好的接口类
class oauthAccount(unittest.TestCase):
    def setUp(self):
        print('测试所有小区列表开始')
        global inter
        inter=interface()
    def test_oauthAccount_1(self):
        """用户名正确"""
        text=oauthAccount(13000000000)
        self.assertEqual(text['message'],'success')
    def test_oauthAccount_2(self):
        """用户名错误"""
        text=inter.oauthAccount(13500000000)
        self.assertEqual(text['message'],'user is error')
    def test_oauthAccount_2(self):
        """用户名为空"""
        text=inter.oauthAccount()
        self.assertEqual(text['message'],'user is null')
    def tearDown(self):
        print('接口测试结束')
