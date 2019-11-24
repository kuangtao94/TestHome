from time import sleep

# pip install pytest-parallel
# pytest-parallel 扩展可以实现测试用例的并行运行

# 不使用线程运行测试用例
# pytest -q test_parallel.py

# 参数‘--tests-per-worker’用来指定线程数，auto 表自动分配
#pytest -q test_parallel.py --tests-per-worker auto

def test_01():
    sleep(3)

def test_02():
    sleep(3)

def test_03():
    sleep(6)