#firtures通常用来对测试方法、测试函数、测试类和整个测试文件进行初始化或还原测试环境
# setup_module/teardown_module:在当前文件中，在所有测试用例执行之前与之后执行，只执行一次;
# setup_function/teardown_function:在每个测试函数之前与之后执行;
# setup/teardown:在每个测试函数之前与之后执行;

# 在当前文件下打开cmd窗口执行:pytest -s test_fixtures_01.py


#功能函数
def multiply(a,b):
    return a * b

#===============Firtures=============
def setup_module(module):
    print('setup_module------------>')

def teardown_module(module):
    print('teardown_module--------->')

def setup_function(function):
    print('setup_function---------->')

def teardown_function(function):
    print('teardown_function-------->')

def setup():
    print('setup---------->')

def teardown():
    print('teardown------->')

#==========测试用例==========
def test_multiply_3_4():
    print('test_numbers_3_4')
    assert multiply(3,4) == 12

def test_multiply_a_3():
    print('test_numbers_a_3')
    assert multiply('a',3) == 'aaa'