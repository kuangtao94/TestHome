import unittest
from selenium import webdriver

class BaiduLink(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get("Http://www.baidu.com")

    def tearDown(self):
        self.driver.quit()

    def test_baidu_news(self):
        """百度首页：点击新闻链接是否可正常跳转"""
        self.driver.find_element_by_link_text("新闻").click()
        self.assertEqual(self.driver.current_url,"http://news.baidu.com/")

    def test_baidu_map(self):
        """百度首页：点击地图链接是否可正常跳转"""
        self.driver.find_element_by_link_text("地图").click()
        self.assertEqual(self.driver.current_url,"https://map.baidu.com/")

if __name__ == '__main__':
    unittest.main(verbosity=2)

import re
re.findall()
