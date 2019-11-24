from selenium import webdriver
import logging,traceback
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import ddt,unittest,time

#初始化日志对象
logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S",
    filename = "./test-ddt.log",
)

@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    #数据驱动时指定的三个数据，每个数据一个list
    @ddt.data(['郎平','程序员'],['王楠','乒乓球'])
    #解包，将对应的测试数据到testdate和exceptdata
    @ddt.unpack
    def test_dataDrivenByfile(self,testdata,exceptdata):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        try:
            self.driver.find_element(By.ID,'kw').send_keys(testdata)
            self.driver.find_element(By.ID,'su').click()
            time.sleep(3)
            #断言预期数据是否在源码中
            self.assertTrue(exceptdata in self.driver.page_source)
        except NoSuchElementException as  e:
            #使用traceback获取详细的异常信息
            logging.error("查找页面不存在，异常信息："+ str(traceback.print_exc()))
        except AssertionError as e:
            logging.debug('搜索-"%s",期望-"%s",-失败'%(testdata,exceptdata))
        except Exception as e:
            logging.error('未知错误，错误信息：'+str(traceback.print_exc()))
        else:
            logging.debug('搜索-"%s",期望-"%s",-通过'%(testdata,exceptdata))

    def tearDown(self):
        self.driver.quit()


if __name__=="__main__":
    unittest.main(verbosity=2)
