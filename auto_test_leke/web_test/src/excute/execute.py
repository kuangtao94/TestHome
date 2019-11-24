# coding:utf-8
import unittest   #导入单元测试框架
import HTMLTestRunner
import time
from TestCase.auto_test_leke.web_test.config import param       #导入配置文件
from TestCase.auto_test_leke.web_test.src.common.log import log
from TestCase.auto_test_leke.web_test.src.common.auto_email import a_email    #导入发送邮件的类
#导入自定义的测试用例类
from TestCase.auto_test_leke.web_test.src.testcase.oa_chuangjianhetong import hetong
#第一种执行用例的方式:先导入每条脚本，再添加每条测试用例
# suit=unittest.TestSuite    #定义测试套件
#添加测试用例，添加测试用例中test_开头的方法
# suit.addTest(hetong('test_creat_hetong'))



#第二种执行用例的方式：批量导入需要执行的用例   -----自动发现用例
#定义测试用例所在的路径
# test_dir=case_path

suit=unittest.defaultTestLoader.discover(param.case_path,'crm_*.py')


# report_dir=r'D:\python_work\auto_test\web_test\report\\'

#定义生产报告的文件名
now=time.strftime('%y-%m-%d_%H-%M-%S',time.localtime())
report_name=param.report_path+now+'autotest.html'
# 以二进制的方式写入文件，当文件不存在时，会自动创建文件
fp=open(report_name,'wb')
# 定义执行器，使用HTMLRunner来向报告中写入内容
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化生成报告',tester='名字')
runner.run(suit)     #执行测试套件
fp.close()    #关闭生成的文件
email=a_email()     #创建发送邮件的对象
email.send_email(report_name)   #发送邮件
l=log('execute.log')
l.info('text1')




#定义执行器用来执行所有测试套件
# runner=unittest.TextTestRunner()             #定义执行器
# runner.run(suit)                            #执行测试套件
