"""
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
"""    
"""
如：
test = Test()
test.x
当访问x属性时，python会自动调动描述符的__get__()方法，几个参数的内容分别是
self是描述类自身的实例
instance是这个描述符的拥有者所在类的实例，在这里也就是Test类的实例
owner是这个描述符的拥有者所在的类本身
test.x = "X -man"
此操作对x属性进行赋值，调用__set__()的方法，等号右边是 Value 值

"""
"""
class MyDescriptor:
    def __init__(self,fget = 0,fset = 0,fdel = 0):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
    def __get__(self,instance,owner):
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

"""
"""

c = C()
c.x = "X -name"
c.x
c._x

"""
# 定为一个温度类
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

"""
t = Temperature()
t.cel
t.fah




"""
