page/ :用于存放page层的封装
test_dir/: 测试用例目录
test_report/: 测试报告目录
conftest.py : pytest配置文件
run_tests.py :测试运行文件

命名与设计规范:
1.对于page层的封装存放于page/目录，命令规范为‘xxx_page.py’
2.对于测试用例的编写存放于test_dir/目录，命名规范为‘test_xxx.py’
3.每一个功能点对应一个测试类，并且以‘Test’开头，如‘TestLogin TestSearch’等
4.在一个测试类下编写功能点的所有的测试用例，如‘test_login_user_null’、‘test_login_pwd_null’及‘test_login_success’等

pip install -r requirements.txt

selenium :web ui自动化测试
pytest :Python第三方单元测试框架
pytest-html :pytest扩展，生成HTML格式的测试报告
pytest-rerunfailures :pytest扩展，实现测试用例运行失败重跑
click :命令行工具开发库
poium :基于selenium/appium 的Page Object测试库