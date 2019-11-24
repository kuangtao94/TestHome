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
