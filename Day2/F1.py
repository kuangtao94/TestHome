# import unittest_1
# print(help(unittest_1))

import unittest_1
import requests
import json
import time

class Test_Kuaidi(unittest_1.TestCase):
    def setUp(self):
        self.headers = {
            "User - Agent": "Mozilla / 5.0(Windows NT 6.1; Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 71.0.3578.98  Safari / 537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "lang=zh-cn; theme=default; sid=epn9ornn9fumq3lokiihom2uj5; UM_distinctid=16851836daa0-0202d831821713-5d1f3b1c-100200-16851836dab749; CNZZDATA1254194234=378514718-1547553066-%7C1547553066",
            "Referer":"http://www.kuaidi.com/"
        }
        self.data = {
            "geetest_challenge":"5594a3f5d665b38b9655b37ef415a1d3ll",
            "geetest_validate":"8ee2a8e2e4c25cd20cc6e3b0da597716",
            "geetest_seccode":"8ee2a8e2e4c25cd20cc6e3b0da597716|jordan"

        }

    def test_baishi(self):
        danhao = "71589211836053"
        kd = "huitongkuaidi"
        self.url = "http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html "%(danhao,kd)
        print(self.url)
        self.s = requests.session()
        # 第一步发请求
        r = self.s.post(url=self.url,headers = self.headers,data = self.data)
        print(r.json())
        #第二步获取结果
        print(result["company"])
        data = result["data"]
        print(data[0])
        get_result = data[0]["context"]
        print(get_result)
        #断言：测试结果与期望结果
        self.assertEqual("百世汇通",result["company"])
        self.assertIn("已签收",get_result)

"""断言"""
# class Test(unittest_1.TestCase):
#     def test01(self):
#         a = 1
#         b = 1
#         self.assertEqual(a,b)
#
#     def test02(self):
#         a = "Hello"
#         b = "Hello wrold"
#         self.assertIn(a,b)
#
#     def test03(self):
#         a = True
#         self.assertTrue(a)
#
#     def test04(self):
#         a = "上海"
#         b = "yoyo"
#         self.assertNotEqual(a,b)

# class Test(unittest_1.TestCase):
#
#     def setUp(self):
#         print("start")
#
#     def tearDown(self):
#         print("end")
#
#     def test_001(self):
#         print("执行测试用例1")
#
#     def test_002(self):
#         print("执行测试用例2")
#
#     def test_003(self):
#         print("执行测试用例3")
#
#     def addTest(self):
#         print("Add")


# class IntegerArithmeticTestCase(unittest_1.TestCase):
#     def testAdd(self):  # test method names begin with 'test'
#         self.assertEqual((1 + 2), 3)
#         self.assertEqual(0 + 1, 1)
#
#     def testMultiply(self):
#         self.assertEqual((0 * 10), 0)
#         self.assertEqual((5 * 8), 40)

# class Test(unittest_1.TestCase):   # 测试用例的名称要以test开头
#     def testMiuns(self):
#         """这里是测试减法"""
#         result = 6-5  # 实际结果
#         hope = 1      # 预期结果
#         self.assertEqual(result,hope)
#
#     def testDivide(self):
#         """这是是测试除法"""
#         result = 7 / 2  # 实际结果
#         hope = 3        # 预期结果
#         self.assertEqual(result,hope)

# if __name__ == '__main__':
#     unittest_1.main(verbosity=2)


if __name__ == '__main__':
    unittest_1.main(verbosity=2)