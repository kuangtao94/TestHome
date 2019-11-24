"""def Fun1(x):
    def Fun2(y):
        return x * y
    return Fun2

#闭包的概念：如果在一个内部函数里(Fun2就是这个内部函数)对外部作用域(但不是在全局作用域)的
#变量进行引用(x就是被引用的变量，x在外部作用域Fun1函数里面，但不在全局作用域里)，则这个内部函数(Fun2)就是一个闭包

#在闭包中，外部函数的局部变量对应内部函数的局部变量，事实上相当于之前讲的全局变量跟局部变量的对应关系
#在内部函数中，你只能对外部函数的局部变量进行访问，但不能进行修改

def Fun1():
    x = 5
    def Fun2():
        x *= x
        return x
    return Fun2 
# 程序会报错！

def Fun1():
    x = [5]
    def Fun2():
        x[0] *= x[0]
        return x[0]
    return Fun2


def Fun1():
    x = 8
    def Fun2():
        nonlocal x
        x *= x 
        return x
    return Fun2   
	
# 这个才可以！


count = 5
def fun1():
    global count
    count = 10
    print(count)

# nonlocal 与 global 用法一样，关键字调用，可以对局部变量或者全局变量进行修改！ """

origin = (0, 0)         # 原点
legal_x = [-100, 100]   # x轴的移动范围
legal_y = [-100, 100]   # y轴的移动范围

def create(pos_x=0, pos_y=0):
# 初始化位于原点为主    
    def moving(direction, step):
    # direction参数设置方向，1为向右（向上），-1为向左（向下），0为不移动
    # step参数设置移动的距离
        nonlocal pos_x, pos_y
        new_x = pos_x + direction[0] * step
        new_y = pos_y + direction[1] * step
        # 检查移动后是否超出x轴边界
        if new_x < legal_x[0]:
            pos_x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            pos_x = legal_x[1] - (new_x - legal_x[1])
        else:            
            pos_x = new_x
        # 检查移动后是否超出y轴边界
        if new_y < legal_y[0]:
            pos_y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            pos_y = legal_y[1] - (new_y - legal_y[1])
        else:            
            pos_y = new_y
        return pos_x, pos_y
    return moving
    
move = create()
print('向右移动10步后，位置是：', move([1, 0], 10))
print('向上移动130步后，位置是：', move([0, 1], 130))
print('向左移动10步后，位置是：', move([-1, 0], 10))

    
    
        
