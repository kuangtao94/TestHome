def tirm(s):
    if s=="":
        return s
    elif ((s[0]!="") and (s[-1]!="")):
        return s
    elif s[0]=="":
        s=s[1:]
        return tirm(s)
    elif s[-1]=="":
        s=s[:-1]
        return tirm(s)
    else:
        print(s)


def trim(s):
    if s == '':
        return s          #空字符串直接返回
    while len(s) >= 1:     #循环检查首尾空格并切片删除
        if s[0] == ' ':
            s = s[1:]     #切头部空格
            continue      #循环，连续切头部空格，直到头部无空格
        elif s[-1] == ' ':
            s = s[:-1]
            continue      #连续切尾部空格
        else:
            break         #前后空格都切完退出循环

for ch in "ABC":
    print(ch)
from collections import Iterable
isinstance('abc', Iterable) # str是否可迭代
True
isinstance([1,2,3], Iterable) # list是否可迭代
True
isinstance(123, Iterable) # 整数是否可迭代
False

for i, value in enumerate(['A', 'B', 'C']):
     print(i, value)


# -*- coding: utf-8 -*-
def findMinAndMax(L):
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')
    Run

    def findMinAndMax(L):
        if L != []:
            max = L[0]
            min = L[0]
            for i in L:
                if max < i:
                    max = i
                if min > i:
                    min = i
            return (min, max)
        else:
            return (None, None)



# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s,str)]
print(L2)


# -*- coding: utf-8 -*-
def triangles():
    L = [1]
    yield L
    while True:
        R = [1]
        i = 0
        while i < len(L) - 1:
            R.append(L[i] + L[i + 1])
            i = i + 1
        R.append(1)
        yield R
        L = R


def triangles():
    L = [1]
    while True:
       yield L
       L =  [1] +[L[i] + L[i+1] for i in range(len(L)-1)] + [1]


def add(x, y, f):
    x=-5
    y=6
    f=abs
    return f(x) + f(y)

print(add(-5, 6, abs))
def to_timestamp(dt_str, tz_str):
    cday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    u = re.match(r'UTC([+-]\d+)\:(\d+)', tz_str)
    tz = timezone(timedelta(hours = int(u.group(1)), minutes = int(u.group(2))))
    return cday.replace(tzinfo = tz).timestamp()