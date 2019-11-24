# 非递归函数
"""def function(n):
    relase = n
    for i in range(1,n):
        relase *= i
    return relase
number = int(input("请输入整数："))
relase = function(number)
print("%d的阶梯是:%d"%(number,relase))"""

# 递归函数
def recursion(n):
    if n == 1:
        return 1
    else :
        return n * recursion(n-1)

number = int(input("请输入一个整数："))
result = recursion(number)
print("%d的阶乘是：%d"%(number,result))

"""满足递归的两个条件
1、调用函数本身
2、设置了正确的返回条件
"""
