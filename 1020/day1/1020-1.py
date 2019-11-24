# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# print(driver.title)
# time.sleep(2)
# driver.find_element_by_id("kw").send_keys("taoge")
# driver.find_element_by_id("su").click()
# driver.close()
#
#
# Fad = "FinshC"
# for i in Fad:
#     print(i,end="")
#
# import random
#
# import time
#
#
#
#
# print("-------- 小甲鱼 -----")
# import random
# secret = random.randint(1,10)
# temp = input("猜一猜哪个数字： ")
# guess = int(temp)
# while guess != secret :
#     temp = input("猜一猜哪个数字： ")
#     guess = int(temp)
#     if guess == secret :
#         print("哎呀，你是小甲鱼的蛔虫吗？···")
#         print("猜对了也没有奖励")
#     else :
#         if guess > secret :
#             print("哎呀，大了大了")
#         else :
#             print("哎呀，小了小了")
# print("不玩了不玩了")
#
#
# seore = int(input("请输入分数："))
# while True :
#     seore = int(input("请输入分数："))
#     if 100 > seore >= 90:
#         print("A")
#     elif 90 > seore >= 80:
#         print("B")
#     elif 80 > seore >= 60:
#         print("C")
#     elif seore < 60:
#         print("D")
#     else:
#         print("输入错误")
# print("Good")
#
# Fad = "FinshC"
# for i in Fad:
#     print(i,end="")

# import login,sys,os
# login.login()
# #实现对day2下login文件内容的读取
# path = os.path.dirname(os.path.dirname(__file__))
# file = open(os.path.join(path,r"day2/login"),"r")
# file.close()
# print(file.read())

for item in sys.path:
    print(item)