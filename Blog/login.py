import unittest_1
######禁用安全请求警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
######创建class Bolg类
class Blog():
    ####构造析构方法/魔法方法
    def __init__(self,s):
        ## s = requests.session()  ##全局变量
        self.s = s
    def login(self):
        """登录接口"""
        self.url = "https://passport.cnblogs.com/user/signin"
        header = {
            XXXXXXX
        }
