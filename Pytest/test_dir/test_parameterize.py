import pytest
import math

#pytest 参数化
#'base,exponent,expected'用来定义参数的名称。
# 通过数组定义参数时，每一个元组都是一条测试用例使用的测试数据。
# ids参数默认为None，用于定义测试用例的名称
# math模块的pow()方法用于计算(x的y次方)的值

#运行: pytest -v test_parameterize.py
# ‘-v’ 参数增加测试用例冗长

@pytest.mark.parametrize(
    'base,exponent,expected',
    [
        (2,2,4),
        (2,3,8),
        (1,9,1),
        (0,9,0),
    ],ids=['case1','case2','case3','case4']
)
def test_pow(base,exponent,expected):
    assert math.pow(base,exponent) == expected