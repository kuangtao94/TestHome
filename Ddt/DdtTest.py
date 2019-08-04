from ddt import ddt,unpack,data
import unittest_1
import HTMLTestRunner
import os
import time

@ddt
class TestCases(unittest_1.TestCase):
    def setUp(self):
        print("每条case之前都会执行这个方法")

    def tearDown(self):
        print("每条case之后都会执行这个方法")

    @data(1,2,3)
    def test_testcase_01(self,value):
        print("这是第一条用例")
        try:
            self.assertTrue(value)
            print("test pass")
        except Exception as e:
            print("出错了，错误的结果为%s"%e)
            print("test failed")
            raise e

    @data((1,1),(1,2),(2,2))
    @unpack
    def test_testcase_02(self,value1,value2):
        print("这是第二条用例")
        try:
            self.assertEqual(value1,value2)
            print("test pass")
        except Exception as e:
            print("出错了，错误的结果为%s"%e)
            print("test failed")
            raise e

# if __name__ == '__main__':
#     unittest_1.main()
def getsuite():
    # suite = unittest_1.TestSuite() #测试套件
    # loader = unittest_1.TestLoader()
    # return suite.addTest(loader.loadTestsFromTestCase(TestCases))
    suite = unittest_1.TestLoader.discover(
        start_dir=os.path.dirname(__file__),
        pattern="DdtTest.py",
        top_level_dir=None
        )
    return suite

def getnowtime():
    # report_dir = "./Test_report"
    # now = time.strftime("%Y-%m-%d %H-%M-%S")
    # reportname = report_dir + "/" + now + "Test_report.html"
    # return reportname
    return time.strftime("%Y-%m-%d %H-%M-%S",time.localtime(time.time()))

def run():
    # with open(Report(),"wb") as file:
    #     runner = HTMLTestRunner.HTMLTestRunner(
    #         stream=file,
    #         title="Model test report",
    #         description="Hello testers This is the description of Model test")
    #     runner.run(getsuite())
    file = os.path.join(os.path.dirname(__file__),"Report",getnowtime()+"testReport.html")
    HTMLTestRunner.HTMLTestRunner(
        stream=(open(file,"wb")),
        title="自动化测试报告",
        description="自动化详细测试报告"
        ).run(getsuite())

if __name__ == '__main__':
    run()