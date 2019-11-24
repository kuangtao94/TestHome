"""
生成器  yield 放置函数的位置
不需要类 和 对象方法
def  myGre():
    print("生成器...")
    yield 1
    yield 2
for 循环会自动调用next() 和 处理异常 StopIteration
for i in myGre():
    print(i)

斐波那契数列也可以用生成器来实现
def fibs():
    a = 0
    b = 1
while True:
    a , b = b ,a + b
    yield a

for echo in fibs():
    if echo > 20:
        break
    print(echo)

列表推导式、字典推导式、集合推导式、元组推导式、(字符串推导式 不行)
list = [i for i in range(100) if not(i % 2) and i % 3]
列表推导式是100以内能够被2整除，但不能够被3整除的所有整数！
dict = {i : i %2 == 0 for i in range(10)}  字典
set = {i for i in (1,1,2,3,4,4,5,6,6,7,8,3,4,6,8,9,0)}  集合
tuple = (i for i in range(10))


迭代器
一个容器如果是迭代器，那就必须实现__iter__()魔法方法，返回的结果是迭代器的本身
__next__()魔法方法，它决定了迭代的规则
#定义一个斐波那契数列
class Fibs:
    def __init__(self,n = 20):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b ,self.a + self.b
        if self.a > self.n:
            break
        return self.a
fibs = Fibs()
for echo in fibs:
    if echo < 20:
        print(echo)
    else：
        break































property 描述类
描述类就是将某种特殊类型的类的实例指派给另一个类的属性
特殊类型的类 里面定义__get__()/__set__()/__delete__()三种特殊方法中的任意一个
__get__() 用于访问属性，它返回属性的值
class MyDescriptor:
    def __get__(self,instance,owner ):
        print("getting...",self,instance,owner)
    def __set__(self,instance,value):
        print("setting...",self,instance,value)
    def __delete__(self,instance):
        print("delete...",self,instance)
class Test:
    x = MyDescriptor()

如：
test = Test()
test.x
当访问x属性时，python会自动调动描述符的__get__()方法，几个参数的内容分别是
self是描述类自身的实例
instance是这个描述符的拥有者所在类的实例，在这里也就是Test类的实例
owner是这个描述符的拥有者所在的类本身
test.x = "X -man"
此操作对x属性进行赋值，调用__set__()的方法，等号右边是 Value 值


class MyDescriptor:
    def __init__(self,fget = 0,fset = 0,fdel = 0):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    del __get__(self,instance,owner):
        return self.fget(instacne)
    def __set__(self,instance,value):
        self.fset(instance,value)
    def __delete__(self,instance):
        self.fdel(instance)
class C:
    def __init__(self):
        self._x = None
    def getX(self):
        return self._x
    def setX(self,value):
        self._x = value
    def delX(self):
        del self._x
    x = MyDescriptor(getX,setX,delX)

c = C()
c.x = "X -name"
c.x
c._x


定为一个温度类
class Celsius:
    def __init__(self,value = 30):
        self.value = float(value)
    def __get__(self,instacne,owner):
        return self.value
    def __set__(self,instance,value):
        self.value = float(value)
class Fahrenheit:
    def __get__(self,instance,owner):
        return instacne.cel * 1.8 + 32
    def __set__(self,instance,value):
        instance.cel = (float(value) - 32) / 1.8

class Temperature:
    cel = Celsius()
    fah = Fahrenheit()

t = Temperature()
t.cel
t.fah




"""



#定制时间操作
import  time as t
# 由于localtime返回的时间是字符串的形式返回的  年月日时分秒
class MyTimer:
#使用魔法方法__init__,所有实例对象的变量只要在__init__里面定义，就可以直接调用
    def __init__(self):
        #给初始化赋值方便我们知晓输出数字
        self.uint = ["年","月","天","时","分","秒"]
        self.prompt = "未开始计时"
        self.lasted = []
    # 给属性初始化赋值为0 这里不用start和stop 是由于属性与方法相同，属性的值会覆盖方法！
        self.begin = 0
        self.end = 0
#使用魔法方法进行定位方法 __str__() 和 __repr__()
    def __str__(self):
        return self.prompt
    __repr__ = __str__
#开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示，请先调用stop()方法结束计时"
        print("计时开始！")
#结束计时
    def stop(self):
        if not self.begin:
            print("提示，请先调用start()方法结束计时")
        else:
            self.end = t.localtime()
            self._calc()
            print("结束计时")
#使用内部方法，计算运行时间
    def _calc(self):
        #定义一个运行结果的列表
        self.lasted = []
        self.prompt = "总共运行了"
        #使用迭代进行挨了传输
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            #假如lasted列表为 0 0 0 0 0 秒时,输出运行结果为秒
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.uint[index])
        #为下一轮计算进行初始化变量
        self.begin = 0
        self.end = 0
# 最后再进行两个计时器返回时间和相加
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.uint[index])
        return prompt



#BIF 内置函数
class A:
    pass
class B(A):
    pass
class C:
    pass  # 占位
#如果第一个参数class是第二个参数classinfo的子类，则返回True，否则返回False
issubclass(B,A)
#一个类被认为是其自身的子类
issubclass(B,B)
#classinfo可以是类对象组成的元组，只要class是其中任何一个候选类的子类，则返回True
issubclass(B,object)  #object 是所有类的基类
#引用其他类作为classinfo，返回结果为False
issubclass(B,C)
#在其他情况下，会抛出一个TypeError异常

b = B()
#如果第一个参数(object)是第二个参数(classinfo)的实例对象，则返回True，否则返回Falae
isinstance(b,B)
#如果object是classinfo的子类的一个实例，也符合条件
isinstance(b,A)
#如果第一个参数不是对象，则永远返回False
isinstance(b,C)
#classinfo可以是类对象组成的元组，只要object是其中任何一个候选对象的实例，则返回True
isinstance(b,(A,B,C))
#如果第二个参数不是类或者由类对象组成的元组，会抛出一个TypeError异常






class Tuele:
    def __init__(self,x):
        self.num = x
class Finsh:
    def __init__(self,x):
        self.num = x
class Pool:
    def __init__(self,x,y):
        #实例化对象，把需要的类放进去实例化，实例化里面放入参数(属性！)
        self.tuele = Tuele(x)
        self.finsh = Finsh(y)
    def print_num(self):
        print("有%d个乌龟和%d条鱼"%(self.tuele.num,self.finsh.num))

pool = Pool(1,20)
pool.print_num()



class A :
    def gg(self,name):
        self.name = name
    def bb(self):
        print("我是谁！%s"%self.name)
a = A()
a.gg("nishui")
a.bb()


class A():
    def __init__(self):
        print("进入A…")
        print("离开A…")


class B(A):
    def __init__(self):
        print("进入B…")
        super().__init__()
        print("离开B…")


class C(A):
    def __init__(self):
        print("进入C…")
        super().__init__()
        print("离开C…")


class D(B, C):
    def __init__(self):
        print("进入D…")
        super().__init__()
        print("离开D…")


d = D()


#封装 / 继承 / 多态
'''list = [1,3,5,7,2,5,8]
class mylist(list):
    pass
list1 = mylist()
list1.append(1)
list1.append(4)
list1.append(7)'''


# 实例继承代码！
import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)
    def move(self):
        self.x -= 1
        print("我的位置是：",self.x,self.y)
class Goldfish(Fish):
    pass
class Carp(Fish):
    pass
class Salmon(Fish):
    pass

fish = Fish()
fish.move()
goldfish = Goldfish()
goldfish.move()
carp = Carp()
carp.move()
salmon = Salmon()
salmon.move()

class Shark(Fish):
    def __init__(self):
  #      Fish.__init__(self)
  #使用到super函数，可以帮助我们找到基线的位置，可以自动帮你找出来！
        super().__init__()
        self.hungry = True
    def eat(self):
        if self.hungry :
            print("吃货的梦想就是天天有得吃！")
            self.hungry = False
        else:
            print("饱了，吃饱了！")
shark = Shark()
shark.move()
shark.eat()

#多重继承

class Base1:
    def foo1(self):
        print("我是foo1....我在Base1中")

class Base2:
    def foo2(self):
        print("我是foo2....我在Base2中")

class C(Base1,Base2):
    pass

c = C()
c.foo1()
c.foo2()


class Mylist:
    def __init__(self,name):
        self.name = name
    def div(self):
        print("我叫%s"  %self.name)

tt = Mylist("hah")
tt.div()




class Ball:
    def setName(self,name):
        self.name = name
    def dick(self):
        file_name = "涛哥"
        self.autuor = file_name
        print("我的名字叫%s ，噢！谁踢我！" % self.autuor)
a = Ball()
a.setName("飞火流星")
b = Ball()
b.setName("团队之星")
c = Ball()
c.setName("马铃薯")
a.dick()
b.dick()
c.dick()

# 对象 = 属性 + 方法
class Turtle:
    #python 中类的名以大写的字母开头
    #特性的描述称为属性，在代码层面来看其实就是变量
    color = "green"
    weight = 10
    legs = 4
    shell = True
    mouth = "大嘴"
    # 方法其实就是函数，通过调用这些函数来完成某些工作
    def climb(self):
        print("我正在努力的向前爬")
    def run(self):
        print("我正在飞快的向前跑")
    def bite(self):
        print("咬死你咬死你")
    def eat(self):
        print("有的吃，很满足")
    def sleep(self):
        print("困了，睡觉，晚安！")
# 创建一个对象，也叫类的实例化，给类赋值给定义的变量
tt = Turtle()
tt.bite()
tt.climb()
tt.eat()
tt.sleep()


from  easygui import  EgStore
#定义一个Settings的类,来继承EgStore的类
class Settings(EgStore):
    def __init__(self,filename): #需要指定文件名
        # 有变量的话为形式参数  有常量的话为实际参数
        #需要记住属性名称
        self.author = ""
        self.book = ""

        #必须执行下面两个语句
        self.filename = filename
        self.restore()

#创建一个Settings实例化的对象settings
settingsFilename = "settings.txt"
settings = Settings(settingsFilename)

author = "小甲鱼"
book = "《零基础入门学习Python》"

#将上面两个变量的值保存到settings对象中
settings.author = author
settings.book = book
settings.store()
print("\n保存完毕\n")

try:
    print("I love FishC")
    int("FISHC")
except:
    exceptionbox()

def tset(name,file):
    print(name + "--->" + file)

tset("5","6")












import easygui as g
msg = "请问你希望在鱼C工作室学习到什么知识呢?"
title = "小游戏互动"
choices = ["谈恋爱","编程","索泡","琴棋书画"]
g.buttonbox('大家说我长得帅吗？', image='taoge.jpg', choices=('帅', '不帅', '!@#$%'))
g.multchoicebox(msg = "你到底想干嘛！",title = "为什么？",choices = ('帅', '不帅', '!@#$%'))
g.textbox(msg = "显示文本内容",title = " ",text="卧槽，尼玛，你谁呀！",codebox = True)
g.codebox(msg = "" ,title = " " ,text = "")
file = g.fileopenbox(msg = "",title = "",default= "*",filetypes=".py")
print(file)
filesave = g.filesavebox(msg = "",title = "",default="*.txt")
print(filesave)
dir = g.diropenbox(msg = "请选择一个文件夹",title = "浏览文件夹")
print(dir)
#root = g.multpasswordbox(msg = "请输入用户名和密码",title = "")
pwd = g.passwordbox(msg = "请输入密码",title = "")
print(pwd)
#g.multenterbox(msg = "请输入",title = "")
g.integerbox(msg,title)
g.enterbox(msg,title)
g.ynbox(msg,title)
g.buttonbox(msg,title,choices)
g.indexbox(msg,title)

import easygui
easygui.msgbox("嗨，美女！")
from easygui import *
msgbox("嗨，大家好！",ok_button="好")
import easygui as g
import sys
while 1:
    g.msgbox("嗨，欢迎进入第一个界面小游戏")
    msg = "请问你希望在鱼C工作室学习到什么知识呢?"
    title = "小游戏互动"
    choices = ["谈恋爱","编程","索泡","琴棋书画"]
    choice = g.choicebox(msg,title,choices)
    g.msgbox("你的选择是："+ str(choice),"结果")
    msg = "你希望重新开始游戏吗？"
    title = "请选择"
    if g.ynbox(msg,title):
        pass
    else:
        sys.exit(0)

g.msgbox("哈哈哈")


try:
    with open(r"D:\Program Files\python36\tes.txt") as f :
        for echo_line in f:
            print(echo_line)
except OSError as reason:
    print("出错啦：" + str(reason))
    print(type(reason))


try:
    int("666")
except ValueError as reason:
    print("出现错误的原因：" + str(reason))
else:
    print("没有任何异常！")



def showMaxFactor(num):
    count = num // 2
    while count > 1:
        if num % count == 0:
            print("%d的最大约数是%d" %(num,count))
            break
        count -= 1
    else:
        print("%d是一个素数" %num)
        #return
num = int(input("请输入一个数："))
print(showMaxFactor(num))



import os
#print(9 // 2)
# raise 抛出异常结果！
raise ZeroDivisionError("除数不能为零")
#异常处理机制 ：
# try .. except .. finally 或者 except OSError as reason：
try:
    file = open(r"D:\Program Files\python36\test.txt")
    print(file.read())
    sum = 1 + "1"
except:
    print("错误啦")
finally:
    file.close()






file_name = input("请输入你要打开的文件：")
f = open(file_name)
print("打开的文件内容为：")
for echo_line in f :
    print(echo_line)


print("="*12,"学员管理系统","="*14)
print("{0:1} {1:13} {2:15}".format(" ","1.查看学员信息","2.添加学员信息"))
print("{0:1} {1:13} {2:15}".format(" ","3.删除学员信息","4.退出系统"))
print("="*40)