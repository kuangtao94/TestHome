# coding:utf-8
# 面向对象与面向过程
class car():          #定义 类
    lunzi=4
    color='green'
    def run(self):
        print('车载炮')

class littlecar(car):            #子类调用父类，可以继承父类
    ranliao='汽油'
    renshu=5
    def jiasu(self):
        print('跑的很快')
print(__name__)
if __name__ == '__main__':
    byd=car()
    byd.run()                      #创建对象
    bmw=car()
    benz=car()
    print(byd.color)
    kading=littlecar()                    #创建对象，指类的实例化
    kading.jiasu()
    print(kading.ranliao)
    print(byd.lunzi)
    print(byd.color)

#变量的作用域
# class bianliang():
#     # global a,b             #使用global将变量强制声明全局变量
#     def __init__(self,c,d):        #类的初始化在创建对象时执行的，参数要在创建对象时赋值
#             self.a=c                    #先声明再赋值，全局变量声明可以在类或者方法中
#             self.b=d
#     def jiafa(self):
#             # global a,b
#             # a=4           #局部变量
#             # b=3
#         return self.a+self.b
#     def jianfa(self):
#             # a=9
#             # b=6
#         return self.a-self.b
#     def chengfa(self):
#         print(self.jiafa()*self.jianfa())
#
# a=bianliang(100,20)
# a.chengfa()










