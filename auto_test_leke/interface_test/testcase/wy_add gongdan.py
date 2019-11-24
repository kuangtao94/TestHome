# coding:utf-8
import requests                #可以使用代码发送http请求
import json                    #用来处理json数据
import unittest
from TestCase.auto_test_leke.interface_test.interface.interfacejb import interface   #导入封装好的接口类
class buildingInfoList(unittest.TestCase):
    def setUp(self):
        print('测试查询工单接口开始')
        global inter
        inter=interface()
    def test_buildingInfoList_1(self):
        """用户名正确，密码正确，查询工单成功"""
        text=inter.buildingInfoList(13000000000,123456)
        self.assertEqual(text['message'],'success')
    def test_buildingInfoList_2(self):
        """用户名错误，密码正确，查询工单失败"""
        text=inter.buildingInfoList(13500000000,123456)
        self.assertEqual(text['message'],'user is error')
    def test_buildingInfoList_2(self):
        """用户名正确，密码错误，查询工单失败"""
        text=inter.buildingInfoList(13500000000,23456)
        self.assertEqual(text['message'],'password is error')
    def tearDown(self):
        print('接口测试结束')