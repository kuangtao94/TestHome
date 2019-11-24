#!/usr/bin/env python
#-*- conding:utf-8 -*-
# Teacher Tao

# def div(a,b):
#     return a/b
# try:
#     div(1,8)
# except ZeroDivisionError as e:
#     print(e.args)
#
# # 分母为零的情况
# try:
#     div(1,0)
# except Exception as e:
#     print(e.args)
#
# # 分母为字符串的情况
# try:
#     div(1,"adad")
# except Exception as e:
#     print(e.args)


"""
try -- except -- else -- fianlly
1.先执行 try -- 不合适 执行 except
2.try -- else -- 最后执行 finally 
"""

try:
    pass
except Exception as e:
    pass
else:
    pass
finally:
    pass


# # 模拟注册
# # 模拟登录
# # 模拟登录成功后显示登录昵称
#
# import json
#
#
# def typeUsername():
#     username = input(u"请输入账号：\n")
#     return username
#
# def typePassword():
#     password = input(u"请输入密码：\n")
#     return password
#
# def regetist(username,password):
#
#     """
#     实现注册的功能
#     :parameter username: 注册系统账号
#     :parameter password: 注册系统密码
#     """
#     temp = username + "|" + password
#     #实现文件的序列化操作
#     file = json.dump(temp,open("login.txt","w"))
#
# def login(username,password):
#     """
#     登录
#     :parameter username:登录系统的账号
#     :parameter password:登录系统的密码
#     """
#     file = str(json.load(open("login.txt","r")))
#     list1 = file.split("|")
#     if list1[0] == username and list1[1] == password:
#         return True
#     else:
#         return False
#
# def info(username,password):
#     """
#     登录成功后显示的昵称
#     :parameter username: 登录系统的账号
#     :parameter password: 登录系统的密码
#     """
#     file = str(json.load(open("login.txt", "r")))
#     list2 = file.split("|")
#     r = login(username, password)
#     if r:
#         print(u"恭喜{0}进入到系统".format(list2[0]))
#     else:
#         print(u"sorry，登录失败！")
#
# def exit():
#     # 退出系统
#     import sys
#     sys.exit()
#
# def main():
#     while True:
#         try:
#             t = int(input(u"1.注册，2.登录，3.退出系统\n"))
#             if isinstance(t,float):
#                 t = int(t)
#         except Exception as e:
#             print(e.args)
#         else:
#             if t == 1:
#                 username = typeUsername()
#                 password = typePassword()
#                 print("注册成功")
#                 regetist(username,password)
#             elif t == 2:
#                 username = typeUsername()
#                 password = typePassword()
#                 login(username,password)
#
#                 info(username,password)
#             elif t == 3:
#                 exit()
#             else:
#                 print(u"输入错误，请重新输入")
#         finally:
#             pass
#
# if __name__ == "__main__":
#     main()


# 模拟注册
# 模拟登录
# 模拟登录成功后显示登录昵称

import json

def typeUsername():
    username = input(u"请输入账号：\n")
    return username

def typePassword():
    password = input(u"请输入密码：\n")
    return password

def regetist(username,password):

    """
    实现注册的功能
    :parameter username: 注册系统账号
    :parameter password: 注册系统密码
    """
    temp = username + "|" + password
    #实现文件的序列化操作
    file = json.dump(temp,open("login.txt","w"))

def login(username,password):
    """
    登录
    :parameter username:登录系统的账号
    :parameter password:登录系统的密码
    """
    file = str(json.load(open("login.txt","r")))
    list1 = file.split("|")
    if list1[0] == username and list1[1] == password:
        return True
    else:
        return False

def info(username,password):
    """
    登录成功后显示的昵称
    :parameter username: 登录系统的账号
    :parameter password: 登录系统的密码
    """
    file = str(json.load(open("login.txt", "r")))
    list2 = file.split("|")
    r = login(username, password)
    if r:
        print(u"恭喜{0}进入到系统".format(list2[0]))
    else:
        print(u"sorry，登录失败！")

def exit():
    # 退出系统
    import sys
    sys.exit()

def main():
    while True:
        try:
            t = int(input("1.注册，2.登录，3.退出系统\n"))
            #如果是float类型的处理
            if isinstance(t,float):
                t = int(t)
            # 字符串类型的处理
            elif isinstance(t,str):
                # 判断字符串是否大于一位，如果是，取出第一位，并且把字母转换为数字
                if len(t) == 1:
                    t = ord(t)
                else:
                    t = int(ord(list(t)[0]))
        except Exception as e:
            print(e.args)

        else:
            if t == 1:
                username = typeUsername()
                password = typePassword()
                print("注册成功")
                regetist(username,password)
            elif t == 2:
                username = typeUsername()
                password = typePassword()
                login(username,password)

                info(username,password)
            elif t == 3:
                exit()
            else:
                print(u"输入错误，请重新输入,请输入1，或者2，或者3")
        finally:
            pass

if __name__ == "__main__":
    main()




