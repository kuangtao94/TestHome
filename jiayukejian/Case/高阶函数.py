# -*- coding: utf-8 -*-
def normalize(name):
    L1=['adam', 'LISA', 'barT']
    L2=list(map(capitalize,L1))
    print(L2)

#  Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。
def prod(x,y):
    return x*y
    reduce(prod,range(1,5))


l2=[1,2,3,4,10]

def prod(l):
    return reduce(fun2,l)
def fun2(x,y):
    return x*y
    print(prod(l2))

s='123.456'

def fun3():
    return map(int,s.split('.')[0]+s.split('.')[1]) #将'123.456'拆分为‘123’，‘456’，在合并成‘123456’，通过map把每个str变成int,

def fun4(x,y):
    return 10*x+y

def str2float():
    a=reduce(fun4,fun3())#得到int类型的123456
    return a/pow(10,len(s.split('.')[1])) # a/10的3次方

    print(str2float())
def is_palindrome(n):
    output = filter(is_palindrome, range(1, 1000))
    print('1~1000:', list(output))
    if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
                                                      101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
        print('测试成功!')
    else:
        print('测试失败!')



def is_palindrome(i):
    i = str(i)
    return i[::3] == i[::-3]
print(list(filter(is_palindrome,range(1,10))))




# -*- coding: utf-8 -*-

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)



def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score)






from functools import reduce

def str2num(s):
    return float(s)




def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()




class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 60 and self.score < 80:
            return 'B'
        if self.score >= 80 and self.score < 110:
            return 'A'
        if self.score >=0 and self.score < 60:
            return 'C'
        else:
            raise ValueError


def fact(n):
    '''
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    3628800
    >>> fact(-1)
    Traceback (most recent call last):
    ...
ValueError
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)
    if __name__ == '__main__':
        import doctest
        doctest.testmod()

fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)


