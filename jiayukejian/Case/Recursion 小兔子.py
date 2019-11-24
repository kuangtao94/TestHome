#用迭代计算20个月后的兔子总数
"""def fan(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print("请重新输入：")
        return -1
    while n -2 > 1:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3
relase = fan(20)
if relase != -1:
    print("总共有%d只小兔子"%relase)

#用递归计算20个月后的兔子总数
def fan(n):
    if n < 1:
        print("请重新输入：")
        return -1
    if n == 1 or n == 2:
        return 1
    else :
        return fan(n-1)+fan(n-2)
relase = fan(2)
if relase != -1:
    print("总共有%d只小兔子"%relase) """

"""n = int(input(">>:"))


def f(n):
    s = 1
    for i in range(2, (n + 1)):
        s *= i
    return s
print(f(n))"""

"""
def factorial_new(n):
 
    if n==1:
        return 1
    return n*factorial_new(n-1)
 
print(factorial_new(5))

"""
"""
def fibNum(n):          #斐波那契数列
    a, b = 0, 1
    for i in range(n):
        b, a = a+b, b
    return b
n = int(input(">>:"))
if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    print(fibNum(n-2)) """


"""
def fibo(n):
    before = 0
    after = 1
    if n == 0 or n == 1:
        return n

    if n <= 3:
        return 1
    return fibo(n-1)+fibo(n-2)

print(fibo(3)) """


def hanno(n,x,y,z):
    # n 为层数  x , y ,z 为柱子
    if n == 1:
        # 从 X 移动到 z
        print(x, "-->", z )
    else:
        hanno(n-1,x,z,y) #从前n-1个盘子移动到y上
        print(x,"-->",z) #从底下64层移动到z
        hanno(n-1,y,x,z) #将Y上的63个盘子移动到Z上

n = int(input("请输入层数："))
print(hanno(n,"X","Y","Z"))
        
        


















    
