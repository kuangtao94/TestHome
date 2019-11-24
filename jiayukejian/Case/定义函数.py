def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
       #在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，
        # 然后，在缩进块中编写函数体，函数的返回值用return语句返回。
# 返回多个值

# 函数可以返回多个值吗？答案是肯定的。

# 比如在游戏中经常需要从一个点移动到另一个点，给出坐标、位移和角度，就可以计算出新的新的坐标：

import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
#    import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。



# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：

# ax2 + bx + c = 0 的两个解。 提示：计算平方根可以调用math.sqrt()函数：
# -*- coding: utf-8 -*-
import math

def quadratic(a, b, c):
    d = b*b-4*a*c
    if d < 0:
        return '无解'
    else:
        x1=(math.sqrt(d)-b) / (2*a)
        x2=(-math.sqrt(d)-b) / (2*a)
        return x1,x2
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(2, 4, 2) =', quadratic(2, 4, 2))
print('quadratic(3, 4, 2) =', quadratic(3, 4, 2))

