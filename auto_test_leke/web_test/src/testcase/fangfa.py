# coding:utf-8


# 使用方法
# def add(a,b):
#     #print(a+b)
#     return a+b
# def jianfa(c,d):
#     return(c-d-add(2,3))
#

# 调用方法
# add(4,5)
# # add('hello',' world')
# print(jianfa(12,2))
#
#
#
# def shuixian(a,b):
#     if 100<=a<b<=1000:
#         for i in range(a,b):
#             if i==(i/100)*(i/100)*(i/100)+((i/10)%10)*((i/10)%10)*((i/10)%10)+(i%10)*(i%10)*(i%10):
#                 print(i)
#     else:
#         print('输入参数不合理')
# shuixian(100,200)
# def liu(*a):
#     print(a)


#冒泡排序
#方法一 while 方法
# a = [78,1,4,5,2,6,34,23,45,3]
# num = len(a) #计算列表的个数
# while num > 0:
#     for i in range(len(a)-1):
#         if a[i] > a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]
#     num -= 1
# print('排序后的列表',a)

#方法二
# a = [78,1,4,5,2,6,34,23,45,3]
# num = len(a) #计算列表的个数
# for i in range(1,num):
#     for j in range(0,num-i-1):
#         if a[j] > a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]
# print('排序后的列表',a)

#水仙花数
# for i in range(100,1000):
#     a = i//100
#     b = i%100//10
#     c = i%10
#     if i == a**3 + b**3 + c**3:
#         print("水仙花数:{}".format(i))

#直角三角形编写
# a = int(input('请输入边长A:'))
# b = int(input('请输入边长B:'))
# c = int(input('请输入边长c:'))
#
# if a >0 and b >0 and c >0:
#     if a + b > c or a + c > b or b + c > a:
#         if a == b or a == c or b == c:
#             if a == b == c:
#                 print('等边三角形')
#             else:
#                 print('等腰三角形')
#         else:
#             print('普通三角形')
#     else:
#         print('不是三角形')
# else:
#     print('输入有误!')











