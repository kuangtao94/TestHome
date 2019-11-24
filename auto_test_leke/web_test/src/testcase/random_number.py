#coding:utf-8
from random import Random    #导入随机数
ran=Random()       #创建随机数的对象
# num=ran.randint(10000000,999999999)         #在1-10范围内产生随机整数
# # print(num)
# print('176%d'%(num))
# for i in range(100):
#     num=ran.randint(100000000,999999999)
#     print('%d@qq.com'%(num))
# base ='abcdefghijklmnopqrstuvwxyz0123456789'
# for i in range(1000):
#     email=''
#     for j in range(ran.randint(5,10)):
#         i=ran.randint(0,len(base)-1)
#         email=email+base[i]
#     print('%s@163.com'%email)

base ='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
for i in range(1000):
    email=''
    for j in range(5):
        i=ran.randint(0,len(base)-1)
        email=email+base[i]
    print('粤B·%s'%email)
