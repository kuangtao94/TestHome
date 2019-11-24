# coding:utf-8
import os
import time

start_time=input('请输入脚本开始时间，例如11:00：')
while True:
    now=time.strftime('%H:%M',time.localtime())
    if now==start_time:
        print('测试开始')
        os.chdir(r'D:\Project\TestCase\auto_test_leke\web_test\src\excute\\')
        os.system('python excute.py')
        print('测试结束')
        break
    else:
        print(now)
        time.sleep(10)
