#coding:utf-8
import time     #获取时间相关
import os      #提供了和操作系统交互的方法
# time.sleep(2)
# os.chdir('C:\Program Files (x86)\Tencent\TIM\Bin')      #切换到程序所在的路径    相当于cmd中sd命令
# os.system('TIM.exe')
# os.chdir(r'D:\python_work\auto_test\lianxi')
# os.system('python random_number.py')
# print(__file__)        #当前脚本的属性
# print(os.path.abspath(__file__))      #获取脚本的路径加文件名
# print(os.path.dirname(os.path.abspath(__file__)))      #获取文件夹下所有的文件
# print(os.listdir(os.path.dirname(os.path.abspath(__file__))))    #获取该文件夹下的所有文件
#
# now=time.strftime('%y-%m-%d_%H:%M:%S',time.localtime())   #将时间转换成字符串格式 ,time.localtime()获取当前系统的时间
# print(now)