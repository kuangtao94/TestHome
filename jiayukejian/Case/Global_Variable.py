def discounts(price,rate):
    Fianl_price = price * rate
   # print("这里试图打印出全局变量的old_price的值：",old_price)
    old_price = 50
    print("这里试图打印出全部变量的old_price的值1：",old_price)
    return Fianl_price

old_price = float(input("请输入价格："))
rate = float(input("请输入汇率："))
new_price = discounts(old_price,rate)
print("打折后的价格：",new_price)
print("这里试图打印出全部变量的old_price的值2：",old_price)

# 全局变量在整个代码中都是可以访问到的，
#但是要试图在函数内部去修改全局变量的值，
#因为那样Python会自动在函数内部新建一个名字一样的局部变量代替
