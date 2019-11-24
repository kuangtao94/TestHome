from TestCase.Poium.baidu_page import BaiduPage
from selenium import webdriver
from time import sleep
import unittest


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

    def test_baidu_search_casel(self):
        '''测试百度搜索'''
        page = BaiduPage(self.driver)
        page.get('http://www.baidu.com')
        page.search_input = 'selenium'
        page.search_button.click()
        sleep(2)
        self.assertEqual(page.get_title,'selenium_百度搜索')

if __name__ == '__main__':
    unittest.main(verbosity=2)


