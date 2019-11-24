# -*- coding: utf-8 -*-
height = input("please your height: ")
weight = input("please your weight: ")
height=float(height)
weight=float(weight)
bmi=weight/height*height
bmi=float(bmi)
if bmi<=18.5:
    print("过轻")
elif bmi<=25:
    print("正常")
elif bmi<=28:
    print("过重")
elif bmi<=32:
    print("肥胖")
else:
    print("严重肥胖")

name = input('please input student\'s name:')
Hight = input('please input %s\'s hight:' %(name))
Weight = input('please input %s\'s weight:' %(name))
Hight = float(Hight)
Weight = float(Weight)
BMI = Weight/(Hight*Hight)
BMI = float(BMI)
if BMI<18.5:
    print('%s\'s BMI is %d,BMI指数低于18.5：体重过轻' %(name,BMI))
elif 18.5<=BMI<25:
    print('%s\'s BMI is %d,BMI指数在18.5-25区间，体重正常' % (name, BMI))
elif 25<=BMI<28:
    print('%s\'s BMI is %d,BMI指数在25-28区间，体重过重' % (name, BMI))
elif 28<=BMI<32:
    print('%s\'s BMI is %d,BMI指数在28-32区间，体重肥胖' % (name, BMI))
else:
    print('%s\'s BMI is %d,BMI指数高于32，体重严重肥胖' % (name, BMI))
print()