import pytest

# 1.运行名称中包含某字符串的测试用例
#名称中含add 的测试用例
# 执行: pytest -k add test_assert.py

# 2.减少测试的运行冗长
# 执行: pytest -q test_assert.py

# 3.如果出现一条测试用例失败，则退出测试
# 执行: pytest -x test_assert.py

# 4.运行测试目录 相对路径或绝对路径都行
# 执行: pytest ./test_dir

# 5.指定测试类或方法执行
# 指定运行test_fixtures_02.py文件中的TestMultiply类下的test_multiply_5_6方法
# 文件名、类名和方法名之间用::符合分隔
# 执行: pytest test_fixtures_02.py::TestMultiply::test_multiply_5_6

# 6.通过main()方法运行测试
# if __name__ == '__main__':
#     if __name__ == '__main__':
#         pytest(['-s','./test_dir'])

#生成测试报告
# 1.生成JUnit XML 文件
# 执行: pytest ./test_dir --junit-xml=./report/log.xml

# 2.生成在线测试报告
# 执行: pytest ./test_dir --pastebin=all

# 3.pytest-html 可以生成HTML格式的测试报告
# 安装 pip install pytest-html
# 执行: pytest ./ --html=./report/result.html
