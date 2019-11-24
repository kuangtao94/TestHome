# pip install pytest-rerunfailures
# pytest-rerunfailures 可以在测试用例失败时进行重试(连跑)

#通过 ‘--reruns’参数设置测试用例运行失败后的重试次数
#执行 pytest -v test_rerunfailures.py --reruns 3

def test_fail_rerun():
    assert  2 + 2 == 5
