#!/usr/bin/env python
#-*- conding:utf-8 -*-
# Teacher Tao
import json
class Login(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def getUserName(self):
        return self.username

    def setName(self,username):
        self.username = username

    def getPasswd(self):
        return self.password

    def setPasswd(self,password):
        self.password = password

    def regetist(self):
        temp = self.username + "|" + self.password
        # 实现文件的序列化操作
        file = json.dump(temp, open("login.txt", "w"))
        print("恭喜你，注册成功！请登录")

    def login(self):
        file =  str(json.load(open("login.txt", "r")))
        list1 = file.split("|")
        if list1[0] == self.username and list1[1] == self.password:
            return True
        else:
            return False

    def info(self):
        file =  str(json.load(open("login.txt", "r")))
        list2 = file.split("|")
        r = self.login()
        if r:
            print(u"恭喜{0}进入到系统".format(list2[0]))
        else:
            print(u"sorry，登录失败！")

    def exit(self):
        import sys
        sys.exit(1)

def main():
    log = Login("user","passwd")
    while True:
        try:
            t = int(input("1.注册，2.登录，3.退出系统\n"))
            # # 如果是float类型的处理
            # if isinstance(t, float):
            #     t = int(t)
            # # 字符串类型的处理
            # elif isinstance(t, str):
            #     # 判断字符串是否大于一位，如果是，取出第一位，并且把字母转换为数字
            #     if len(t) == 1:
            #         t = ord(t)
            #     else:
            #         t = int(ord(list(t)[0]))
        except Exception as e:
            print(e.args)
        else:
            if t == 1:
                log.regetist()
            elif t == 2:
                log.info()
            elif t == 3:
                log.exit()
            else:
                print(u"输入错误，请重新输入")
        finally:
            pass

if __name__ == '__main__':
    main()



