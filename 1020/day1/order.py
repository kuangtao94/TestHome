#使用装饰器实现一个登录功能
"""
1、创建一个字典 ，映射函数
2、创建函数，形参
3、使用 if else 进行判断登录账号密码
4、创建admin登录函数 ，使用if else 进行判断
5、创建order订单函数 ，

LOGIN_USER = {"is_login" : false}
def login(username,password):
    if username == "admin" and password == "admin":
        LOGIN_USER["is_login"] = True
        LOGIN_USER["current_user"] = username
        admin()
    else:
        print("用户名和密码错误")

def admin():
    if LOGIN_USER["is_login"]:
        print("当前登录账号为：%s"%LOGIN_USER["current_user"])
    else:
        print("请先登录！谢谢")

def order():
    if LOGIN_USER["is_login"]:
        print("当前用户为：%s"%LOGIN_USER["current_user"])
    else:
        print("请先登录！谢谢")

def quit():
    if LOGIN_USER["is_login"]:
        print("当前账号为：%s"%LOGIN_USER["current_user"])
    else:
        print("请先登录！谢谢")

def mian():
    while True:
        p = input("1、访问后台系统 2、查看订单 3、退出后台系统 4、登录前台系统 5、退出\n" )
        if p == 1:
            admin()
        elif p == 2:
            order()
        elif p == 3:
            quit()
        elif p == 4:
            username = input("请输入账号：\n")
            password = input("请输入密码：\n")
            login(username,password)
        elif p == 5:
            import  sys
            sys.exit()
if __name__ == "__main__":
    main()

"""





def outer(func):
    def inner():
        if LOGIN_USER["is_login"]:
            r = func()
            return r
        else:
            print("请先登录!谢谢")
    return inner

def f1():
    print("当前登录账号为：%s"%LOGIN_USER["current_user"])

LOGIN_USER = {"is_login" : false}
def login(username,password):
    if username == "admin" and password == "admin":
        LOGIN_USER["is_login"] = True
        LOGIN_USER["current_user"] = username
        admin()
    else:
        print("用户名和密码错误")

@outer
def admin():
    f1()
@outer
def order():
    f1()
@outer
def quit():
    f1()
def mian():
    while True:
        p = input("1、访问后台系统 2、查看订单 3、退出后台系统 4、登录前台系统 5、退出\n" )
        if p == 1:
            admin()
        elif p == 2:
            order()
        elif p == 3:
            quit()
        elif p == 4:
            username = input("请输入账号：\n")
            password = input("请输入密码：\n")
            login(username,password)
        elif p == 5:
            import  sys
            sys.exit()
if __name__ == "__main__":
    main()
