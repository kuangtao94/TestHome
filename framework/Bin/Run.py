import smtplib
import unittest
from email.mime.text import MIMEText
from unitcase.oprationExcel import *
import os

class Runner:
    def __init__(self):
        """创建类实例化"""
        self.excel = OprationExcel()

    def run_suite(self):
        """要执行测试的套件"""
        suite = unittest.TestLoader.discover(
            start_dir=os.path.join(os.path.dirname(os.path.dirname(__file__)),"Test"),
            pattern="Test*.py",
            top_level_dir=None
        )

    def send_mail(self,to_user,sub,content):
        """
        发送邮件内容
        :param to_user:发送邮件的人
        :param sub :主题
        :param content :邮件内容
        :return:
        """
        global send_mail
        global send_user
        global send_passwd
        send_mail = "smtp.sina.cn"
        send_user = "wuya1303@sina.com"
        send_passwd = "admin123"
        message = MIMEText(content,_subtype="plain",_charset="utf-8")
        message["Subject"] = sub
        message["From"] = send_user
        message["To"] = to_user
        server = smtplib.SMTP
        server.connect(send_mail)
        server.login(user=send_user,password=send_passwd)
        server.sendmail(send_mail,to_user,message.as_string())
        server.close()

    def main_run(self):
        """批量执行测试用例"""
        unittest.TextTestRunner().run(self.run_suite())
        content = "通过数{0};失败数{1};通过率{2}".format(
            self.excel.get_success(),
            self.excel.get_fail(),
            self.excel.run_case_rate()
        )
        print('Please wait while the statistics test results are sent in the mail')
        self.send_mail('1512500241@qq.com', '接口自动化测试报告', content)

if __name__ == '__main__':
    print(Runner().run_suite())