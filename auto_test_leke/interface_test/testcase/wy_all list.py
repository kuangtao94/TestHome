# coding:utf-8
import requests                #可以使用代码发送http请求
import json                    #用来处理json数据
import unittest
from TestCase.auto_test_leke.interface_test.interface.interfacejb import interface   #导入封装好的接口类
class allCommunityId(unittest.TestCase):
    def setUp(self):
        print('测试所有小区列表开始')
        global inter
        inter=interface()
    def test_allCommunityId_1(self):
        """用户名正确，密码正确，获取小区列表成功"""
        text=inter.allCommunityId(13000000000,123456)
        self.assertEqual(text['message'],'success')
    def test_allCommunityId_2(self):
        """用户名错误，密码正确，获取小区列表失败"""
        text=inter.allCommunityId(13500000000,123456)
        self.assertEqual(text['message'],'user is error')
    def test_allCommunityId_2(self):
        """用户名正确，密码错误，获取小区列表失败"""
        text=inter.allCommunityId(13500000000,23456)
        self.assertEqual(text['message'],'password is error')
    def tearDown(self):
        print('接口测试结束')
