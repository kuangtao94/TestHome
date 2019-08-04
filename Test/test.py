
"""私有&公共实例"""
class MyClass:
    def PublicMethod(self):
        print("public method")

    def __PrivateMethod(self):
        print("this is private")

    def callPrivateMethod(self):
        self.__PrivateMethod()

my = MyClass()
print(my.PublicMethod())
print(my.callPrivateMethod())
print(my._MyClass__PrivateMethod())


