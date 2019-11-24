"""
python 内置函数介绍

a = -5
print("输出结果为：",abs(a))

str1 = "Python语言"
print("未转换之前类型：",type(str1))
a = bytes(str1,encoding = "utf-8")
print("转换之后类型：",a,type(a))
b = str(a,encoding = "utf-8")
print("bytes类型转换为字符串类型：",b,type(b))

a = 88
print(chr(a))

Python中有join()和os.path.join()两个函数，具体作用如下：
    join()：    连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串
    os.path.join()：  将多个路径组合后返回

一、函数说明
1、join()函数
语法：  'sep'.join(seq)
参数说明
sep：分隔符。可以为空
seq：要连接的元素序列、字符串、元组、字典
上面的语法即：以sep作为分隔符，将seq所有的元素合并成一个新的字符串
返回值：返回一个以分隔符sep连接各个元素后生成的字符串

2、os.path.join()函数
语法：  os.path.join(path1[,path2[,......]])
返回值：将多个路径组合后返回
注：第一个绝对路径之前的参数将被忽略

1、导入随机函数的模块
2、创建一个空的列表
3、for 语句进行迭代输出
4、输出内容添加到创建的空列表中
5、打印
import random
result = []
for i in range(8):
    r = random.randrange(88,100)
    if r == 2 or r == 4:
        num = random.randrange(0,6)
        result.append(str(num))
    else:
        temp = random.randrange(68,78)
        #数字转化为字符串
        result.append((chr(temp)))
print("".join(result))

compile 的作用，把字符串编译成Python代码，再由函数eval或者exce()来执行
s = 'print("123")'
a = compile(s,"<string>","exec")
exec(a)
"""



