#!/usr/bin/env python
#-*- conding:utf-8 -*-
# Teacher Tao

# class Person(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age
#
#     def setName(self, name):
#         self.name=name
#
#     def setAge(self,age):
#         self.age=age
#
#     def info(self):
#          return "name{0},age{1}".format(self.name,self.age)
# per = Person("Teacher",24)
# per.info()
# print(per.info())

"""
首先一个类，不管是否写了构造函数，它都是有构造函数的
一个类，可以有多个构造函数,建议一个类只有一个构造函数
构造函数
1.初始化属性
"""
# class Person1(object):
# #动态方法
#     def __init__(self,*args,**kwargs):
#         self.args = args
#         self.kwargs = kwargs
#
#     def info(self):
#         # print("信息:",self.kwargs)
#         print("信息:",self.args)
#
# per1 = Person1(name="Teacher",age=24)
# per1 = Person1("Teacher",26)
# per1.info()
# per1.info()


"""
析构函数
对象实例化-->构造函数-->对象调用方法-->代码跳转到具体的方法
-->执行方法的代码块-->最后执行析构函数
"""
# class Person(object):
#     def __init__(self):
#         print("我是构造方法")
#
#     def __del__(self):
#         print("我是析构方法")
#
#     def info(self):
#         print("我是方法")
#
# per = Person()
# per.info()
#

"""
普通方法
"""
# class Person2(object):
#     def conn(self,user,passwd,host,port):
#         pass
#
#     def f1(self,*args,**kwargs):
#         # self.kwargs = kwargs
#         # self.args = args
#         pass
#
#     def info(self):
#         print("我是普通方法")
#
# per = Person2()
# per.conn("root",123456,"localhost",3306)
# per.info()

"""
特性方法：不能有形式参数
"""
# class Person(object):
#
#     @property #装饰器
#     def getUserID(self):
#         pass
#
# per = Person()
# per.getUserID   #不加(),加()报错

# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.find_element_by_id("kw").text

"""
静态方法:
可以直接使用类名来调用方法，属于类
实例对象也可以调用方法，但不建议使用，多此一举！
"""
# class MySQL(object):
#     @staticmethod
#     # 方法参数不用加self
#     def conn(user):
#         pass
#
# # MySQL.conn("Teacher")
# sql = MySQL()
# sql.conn("Teacher")

"""
类的方法：直接使用类名来调用
"""
# class MySQL(object):
#     @classmethod
#     # 方法参数不用加self
#     def conn(cls):
#         pass
#
# # MySQL.conn("Teacher")
# MySQL.conn()

"""
属于类：
     类属性
     静态方法
     类方法
属于对象：
       实例属性
       普通方法
       特性方法
"""

"""
类的继承：重复使用已经存在的数据和行为，减少重复编写代码，
子类继承父类的实例属性和方法
"""
"""类属性的继承"""
# class Person(object):
#     China = "中国"
# class UsaPerson(Person):
#     pass
# Usa = UsaPerson()
# Usa.China
# print(Usa.China)

"""实例属性的继承与继承的两种写法"""
# class Fruit(object):
#     def __init__(self,name):
#         self.name = name

"""子类由于业务的需求，需要继承父类的实例属性"""

# class Apple(Fruit):
#     def __init__(self,name,brand,color):
# #        super(Apple,self).__init__(name)
#         Fruit.__init__(self,name)
#         self.brand = brand
#         self.color = color
#
#     def info(self):
#         return "名称{0},品牌{1},颜色{2}".format(self.name,self.brand,self.color)
#
# app = Apple("苹果","富士","红色")
# app.info()
# print(app.info())

# class Fruit(object):
#     def __init__(self,name):
#         self.name = name
"""子类由于业务的需求，不需要继承父类的实例属性"""

# class Apple(Fruit):
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color
#
#     def info(self):
#         return "品牌{0},颜色{1}".format(self.brand,self.color)
#
# app = Apple("富士#","红色")
# app.info()
# print(app.info())

"""格式化字符"""
#"{a} Love {b}.{0}".format(a = "I",b = "You","com")
"{0} Love {a}.{b}".format("I",a = "You",b = "com")


"""
方法的继承：
子类为什么要重写父类的方法？子类有自己的特性
当子类重写了父类的方法，对子类进行实例化对象后，
子类调用的(父类，子类方法都存在)方法，执行的方法是子类的方法

"""
# class Person(object):
#     def eat(self):
#         print("人需要吃饭的")
#
# class Son(Person):
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self):
#         print("名字是{0},为什么？".format(self.name))
#
# son = Son("Teacher")
# son.eat()


"""
单个类继承的原则：
1.从上到下，子类继承父类，但没有重写父类的方法，
对子类进行实例化对象后，执行调用是直接父类中的方法
2.从下到上，子类继承父类，但子类重写父类的方法，
对子类进行实例化对象后，执行调用是直接子类中的方法(优先调用自己方法)
"""

# class Fruit(object):
#     def eat(self):
#         print("水果是用来吃的")
#
# class Apple(Fruit):
#     def __init__(self,color):
#         self.color = color
#
#     def eat(self):
#         print("苹果的颜色{0},该吃掉了！".format(self.color))
#
# class Band(Apple):
#     def eat(self):
#         print("我是Apple的子类")
#
# band = Band("红色")
# band.eat()

# class Person(object):
#     def __init__(self,name):
#         self.name=name
#
#     def info(self):
#         print (self.name)
#
# class Son(Person):
#     def info(self):
#         print (self.name)
#
# s=Son('name')
# s.info()
#

"""多个继承：执行的顺序，从左到右执行;并且是同一级别的！同一级别指的是共同的类"""

# class Person(object):
#     def eat(self):
#         print("人是吃饭的")
#
# class Monther(Person):
# #   def eat(self):
# #        print("妈妈不吃饭，要减肥")
#         pass
#
# class Father(Person):
#     def eat(self):
#         print("爸爸吃饭！")
#
# class Son(Monther,Father):
#     pass
#
# son = Son()
# son.eat()


"""__doc__ 打印出类的注释"""

# class Person(object):
#     """人的属性&特性"""
#     def info(self,username,password):
#         """
#         :param username: 参数用户名
#         :param password: 参数密码
#         :return:
#         """
#         pass
#
# per = Person()
# print(per.__doc__)

"""__call__:对象创建时直接返回__call__的内容,使用该方法可以模拟静态方法"""

# class Per(object):
#     def __new__(cls, *args, **kwargs):
#         print("打印出call方法")
#
# per = Per()

"""
__str__:对象代表的含义，返回一个字符串，通过他可以把字符串和对象关联起来，方便某些程序的实现
该字符串表示某个类，实现__str__后，可以直接使用print语句打印出对象，也可以通过str来触发__str__来执行
__str__:
1.对象的意思
2.返回一个字符串，对象和字符串关联起来 -->该字符串可表示一个类
"""
# class Per(object):
#     """我是一个字符串类"""
#     def __str__(self):
#         return self.__doc__
#
# per = Per()
# print(str(per))

class Factory(object):
    def createFruit(self,fruit):
        if fruit == "apple":
            return Apple()
        elif fruit == "banana":
            return Banana()

class Fruit(object):
    def __str__(self):
        return "fruit"

class Apple(object):
    def __str__(self):
        return "apple"

class Banana(object):
    def __str__(self):
        return "banana"

if __name__ == '__main__':
    factory = Factory()
    print(factory.createFruit("apple"))
    print(factory.createFruit("banana"))


"""工厂设计模式在UI中的应用"""
from selenium import webdriver
from appium import webdriver
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.common.by import By

class Factory(object):
    def createWebDriver(self,WebDriver):
        if WebDriver == "web":
            return WebUI(self.driver)
        elif WebDriver == "app":
            return AppUI(self.driver)

class WebDriver(object):
    def __init__(self,webdriver):
        self.webdriver = webdriver

    def __str__(self):
        return "WebDriver"

    def findElement(self,*loc):
        try:
            return self.driver_find_element_By(*loc)
        except NoSuchElementException as e:
            print("Error details:%s",e.args[0])


    def findElements(self,*loc):
        try:
            return self.driver_find_element_By(*loc)
        except NoSuchElementException as e:
            print("Error details:%s",e.args[0])

class WebUI(WebDriver):
    def __str__(self):
        return "web"

class AppUI(WebDriver):
    def __str__(self):
        return "app"

if __name__ == '__main__':
    factory = Factory()
    print(factory.createFruit("web"))
    print(factory.createFruit("app"))