print("-------- 小甲鱼 -----")
import random
secret = random.randint(1,10)
temp = input("猜一猜哪个数字： ")
guess = int(temp)
while guess != secret :
    temp = input("猜一猜哪个数字： ")
    guess = int(temp)
    if guess == secret :
        print("哎呀，你是小甲鱼的蛔虫吗？···")
        print("猜对了也没有奖励")
    else :
        if guess > secret :
            print("哎呀，大了大了")
        else :
            print("哎呀，小了小了")
print("不玩了不玩了")