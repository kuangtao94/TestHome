import pytest
# conftest.py 是pytest特有的本地测试配置文件;
# 既可以用来设置项目级别的Fixture，也可用来导入外部插件，还可以指定钩子函数

#设置测试钩子

@pytest.fixture()
def test_url():
    return 'http://www.baidu.com'

