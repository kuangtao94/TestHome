#pytest 是支持使用测试类的,同样必须以Test开头，注意首字母大写。
# setup_class/teardown_class:在当前测试类的开始与结束时执行，只执行一次;
# setup_module/teardown_module:在每个测试方法开始与结束时执行;
# setup/teardown:在每个测试方法开始与结束时执行;

# 在当前文件下打开cmd窗口执行:pytest -s test_fixtures_02.py


#功能函数
def multiply(a,b):
    return a * b

class TestMultiply:
    #===============Firtures=============
    @classmethod
    def setup_class(cls):
        print('setup_class------------>')

    @classmethod
    def teardown_class(cls):
        print('teardown_class--------->')

    def setup_module(self,module):
        print('setup_module------------>')

    def teardown_module(self,module):
        print('teardown_module--------->')

    def setup(self):
        print('setup---------->')

    def teardown(self):
        print('teardown------->')

    #==========测试用例==========
    def test_multiply_5_6(self):
        print('test_numbers_5_6')
        assert multiply(5,6) == 30

    def test_multiply_b_3(self):
        print('test_numbers_b_3')
        assert multiply('b',3) == 'bbb'