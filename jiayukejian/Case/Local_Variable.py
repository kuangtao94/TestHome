def discounts(price,rate):
    Fianl_price = price * rate
    print("这里试图打印出局部变量的Final_price的值1：",Fianl_price)
    return Fianl_price

old_price = float(input("请输入价格："))
rate = float(input("请输入汇率："))
new_price = discounts(old_price,rate)
print("打折后的价格：",new_price)
print("这里试图打印出局部变量的Final_price的值2：",Fianl_price)

