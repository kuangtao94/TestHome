import unittest
import os
import HTMLTestRunner
import time

#discover批量执行测试用例
def allTests():
    suite = unittest.TestLoader().discover(
        start_dir = os.path.dirname(__file__),
        pattern = "test_*.py",
        top_level_dir = None )
    return suite

def getNowtime():
    return time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))

#生成HTMLTestRunner报告，stream测试报告写入文件存储的区域
def run():
    file = os.path.join(os.path.dirname(__file__),"Report",getNowtime()+"testReport.html")
    with open(file,"wb") as fp:
        HTMLTestRunner.HTMLTestRunner(
            stream = fp,
            title = "自动化测试报告",
            description = "自动化测试报告详细信息"
            ).run(allTests())

if __name__ == '__main__':
    run()

