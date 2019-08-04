import pytest

class Test():
    def setup_function(self):
        print("setup_function:每个用例开始都会执行")

    def teardown_function(self):
        print("teardown_function:每个用例结束都会执行")

    def test_one(self):
        print("正在执行---test_one")
        x = "this"
        assert ("h" in x)

    def test_two(self):
        print("正在执行--test_two")
        x = "Hello"
        assert hasattr(x,'check')

    def test_three(self):
        print("正在执行--test_three")
        a = "Hello"
        b = "Hello World"
        assert (a in b)

if __name__ == '__main__':
    pytest.main(["-s","test_setup.py"])