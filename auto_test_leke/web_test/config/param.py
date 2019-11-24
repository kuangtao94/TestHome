# coding:utf-8
import os
#获取当前项目所在的路径
# os.path.dirname()  获取文件所在的文件夹
project_path=(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))     #获取当前文件所在绝对路径
case_path=project_path+'\\src\\testcase\\'                                    #定义测试用例所在的路径
report_path=project_path+'\\report\\'                                          #定义测试报告所在的路径
img_path=project_path+'\\img\\'                                                #定义截图所在的路径
data_path=project_path+'\\data\\'                                             #定义excel所在的路径
log_path=project_path+'\\log\\'
d_path='D:\python_work'