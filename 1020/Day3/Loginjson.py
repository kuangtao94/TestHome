#!/usr/bin/env python
#-*- conding:utf-8 -*-
# Teacher Tao



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
        t = int(input(u"1.注册，2.登录，3.退出系统\n"))
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
            print(u"输入错误，请重新输入")

if __name__ == "__main__":
    main()
