#!/usr/bin/env python
#-*- conding:utf-8 -*-
# Teacher Tao

"""
函数的返回值：
1、一个函数，它是有返回值的
2、当一个函数，没有return关键字的时候，它的返回值是None
3、当一个函数有return关键字的时候，它的返回值是return后面的表达式或者值

函数的返回值意义：函数/方法的返回值是为了给另外一个函数/方法一个请求参数而已

接口测试：查看用户信息，实现的步骤
1、发送post请求，login请求登录成功
2、登录成功之后，发送Token
3、带着这个Token，可以查看用户信息
"""

# def login(username = "Teacher",password = "admin"):
#     if username == "Teacher" and password == "admin":
#         return "dahaihduandkja2jnakjdn"
#     else:
#         return "login Fail"
# def userInfo(token):
#     """查看用户信息"""
#     if token == "dahaihduandkja2jnakjdn":
#         print("查看订单信息正常")
#     else:
#         print("login out")
#
# userInfo(login())
#
# """
# 模拟注册
# 模拟登录
# 模拟登录成功后显示登录昵称
# """
# def typeUsername():
#     username = input(u"请输入账号：\n")
#     return username
#
# def typePassword():
#     password = input(u"请输入密码：\n")
#     return password
#
# def regetist(username,password):
#     """
#     实现注册的功能
#     :parameter username: 注册系统账号
#     :parameter password: 注册系统密码
#     """
#     temp = username + "|" + password
#     file = open("login.txt","w")
#     file.write(temp)
#
# def login(username,password):
#     """
#     登录
#     :parameter username:登录系统的账号
#     :parameter password:登录系统的密码
#     """
#     with open("login.txt","r") as file:
#         for line in file:
#             list = line.split("|")
#             if list[0] == username and list[1] == password:
#                 return True
#             else:
#                 return False
#
# def info(username,password):
#     """
#     登录成功后显示的昵称
#     :parameter username: 登录系统的账号
#     :parameter password: 登录系统的密码
#     """
#     with open("login.txt","r") as file:
#         for line in file:
#             #把字符串转为list
#             list = line.split("|")
#         r = login(username,password)
#         if r:
#             print(u"恭喜{0}进入到系统".format(list[0]))
#         else:
#             print(u"sorry，登录失败！")
#
# def exit():
#     # 退出系统
#     import sys
#     sys.exit()
#
# def main():
#     while True:
#         t = int(input(u"1.注册，2.登录，3.退出系统\n"))
#         if t == 1:
#             username = typeUsername()
#             password = typePassword()
#             print("注册成功")
#             regetist(username,password)
#         elif t == 2:
#             username = typeUsername()
#             password = typePassword()
#             login(username,password)
#
#             info(username,password)
#         elif t == 3:
#             exit()
#         else:
#             print(u"输入错误，请重新输入")
#
# if __name__ == "__main__":
#     main()

