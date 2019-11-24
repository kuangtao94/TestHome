#!/use/bin/env python
#coding:utf-8

#Author:WuYa

import  logging,os
from selenium import  webdriver
import  unittest

def dirName(filename, filePath='Log'):
    # 定义日志文件 filename = log.md 为存储日志
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), filePath, filename)

def log(log_content):
    # 定义文件
    logFile = logging.FileHandler('logInfo.md', 'a')
    # log格式
    fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
    logFile.setFormatter(fmt)

    # 定义日志
    logger1 = logging.Logger('logTest', level=logging.DEBUG)
    logger1.addHandler(logFile)
    logger1.info(log_content)


class Ui(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.PhantomJS()
        log('初始化浏览器')

    def test_001(self):
        print('测试用例')
        log('开始测试')

    def tearDown(self):
        log('测试结束')
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
