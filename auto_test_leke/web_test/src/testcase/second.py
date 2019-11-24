#coding:utf-8
# a=10
# if a<9 or a==10:
#     print('a的值比9大')
#     print('a的值不确定')
# if a<5:
#     print(a的值小于5)
# a=input('第一边是：')
# b=input('第二边是：')
# c=input('第三边是：')
# if a+b>c and a+c>b and b+c>a:
#     if a==b==c:
#         print('等边三角形')
#     elif a==b or b==c or a==c:
#         print('等腰三角形')
#     else:
#         print('普通三角形')
# else:
#     print('不是三角形')
# for i in range(0,10):
#     if i%2==0:
#         print(i)
# for i in range(0,2018):
#     if i%4==0:
#         if i%100==0:
#             if i%400==0:
#                 print(i)
#         else:
#             print(i)
# for i in range(100,1000):
#     if i==(i/100)*(i/100)*(i/100)+((i/10)%10)*((i/10)%10)*((i/10)%10)+(i%10)*(i%10)*(i%10):
#         print(i)
#
# for i in range(1,10):
#     print('\n')
#     for j in range(1,i+1):
#         print('%sx%s=%s'%(j,i,i*j)),
# for i in (9,8,7,6,5,4,3,2,1):
#     for j in range(1,i+1):
#         print('%sx%s=%d\t'%(j,i,i*j)),
#     print('')
# a=0
# while a<10:
#     print(a)
#     a=a-2
#     if a==-100:
#         break

# a=1
# sum=0
# while a<=100:
#     if a%2==1:
#         sum=sum+a
#     else:
#         sum=sum-a
#     a=a+1
# print(sum)

# a=1
# while a<4:
#     name=raw_input('用户名:')
#     password=raw_input('密码:')
#     if name=='admin' and password=='admin123':
#         print('登录成功')
#         break
#     elif a==3:
#         print('账号被锁定')
#         break
#     else:
#         print('用户名和密码错误，请重新输入')
#     a=a+1

# a='' 空字符串

# m1=[1,3,4,6,4]
# m2=['we','rng','edg']
# m3=[100,'rng',2.12,True]
# m4=['hello',['word',10]]
# m5=[]
# m4[0]='he'
# print(m4)
# m5.append('huawei')
# print(m5)
# m3.insert(1,'hello')
# m3.pop(2)
# a='sd.jsiu'
# print(len(a))
# print(set(m3))  去重
# m4.sort(reverse=true  反转)  排序     作业
# m8=sorted(m4)     不会改变m4
# m4.reverse()      列表的反转
# print(a.split('d'))   以指定的符号对字符串进行分割，并保存到列表中
# m2=['we','rng','edg']
# n=''.join(m2)
# print(n)
# m2[1],m2[2]=m2[2],m2[1]
# print(m2)
# s=u'xxxxxx张飞爱吃肉xxxxxx'
# a=s.find(u'张飞爱吃肉')
# m1=list(s)
# m1[a-2],m1[a-1],m1[a],m1[a+1],m1[a+2],m1[a+3],m1[a+4]=m1[a],m1[a+1],m1[a+2],m1[a+3],m1[a+4],m1[a-1],m1[a-2]
# n=''.join(m1)
# print(n)

#
# sy=[]
# for a in u'张飞爱吃肉':
#     sy.append(s.find(a))
# sl=list(s)
# for b in range(0,len(sl)-1):
#     if b in sy:
#         sl[b-2],sl[b]=sl[b],sl[b-2]
# print(''.join(sy))

# info =  {
#     'name':'jet li',
#     'age':55,
#     'sex':'男',
#     'money':1232.231,
#     'company':{
#         'name':'壹基金',
#         'renshu':12313,
#     }
#         }
# print(info['company']['name'])
# info['aihao']='game'
# print(info)
# print(info.keys())       #获取字典中所有的键
# print(info.values())     #获取字典中所有的值


# 3.使用循环的方式对列表进行从小到大排序
#[0,12,4,99,67,33,2]
# s=[]
# for i in [0,12,4,99,67,33,2]:
#     for j in range(0,12,4,99,67,33,2):
#         i<j
#         if i>=j:
#             s.append()
#         else:
#             s.insert(len(s)-1,b)
# print(s)


# p=[0,12,4,99,67,33,2]

# p.sort()


# for j in range(len(p)):
#     for i in range(0,len(p)-1):
#         if p[i]>p[i+1]:
#             p[i],p[i+1]=p[i+1],p[i]
# print(p)
#
#
# for i in range(0,len(p)-1):
#     for j in range(i+1,len(p)):
#         if p[i]>p[j]:
#            temp=p[j]
#            p[j]=p[i]
#            p[i]=temp
# print(p)


# 三位数：个位十位百位互不相等
# 把所有满足条件的三位数，写入到列表中
# 1.将求指定三位数的步骤封装到方法中
# 方法携带两个参数，分别是三位数取值的左右区间，
# 返回结果列表
# 将上述方法封装到类中

# def he(a,b):
#     for i in range(a,b):
#         q=i/100
#         w=i/10%10
#         e=i%10
#         if a!=b and a!=c and c!=b:
#     return i


#
# class sss():
#     def ss(self,a,b):
#         if 100<=a<b<=1000:
#             s=[]
#             for i in range(a,b):
#                 q=i/100
#                 w=i/10%10
#                 e=i%10
#                 if q!=e and q!=w and e!=w:
#                     s.append(i)
#             return s
#         else:
#             print('输入参数不合理')
# liu=sss()
# print(liu.ss(100,1000))

# for i in range(1,5):
#     for j in range(1,5):
#         print('%d %d'%(i,j))
#     print('')

#
# a=raw_input("请输入三个数：").split(",")
# for i in range(len(a)-1):
#     for j in range(len(a)-1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1]=a[j+1],a[j]
#
# print(a)

# a=0
# for i in range(1,100):
#     if i%2==1:
#         a=a+i
#     else:
#         a=a-i
# print(a)
#


# a=input('第一个数:')
# b=input('第二个数:')
# c=input('第三个数:')
# s=[a,b,c]
# for i in range(0,len(s)):
#     for j in range(i+1,len(s)):
#         if s[i]>s[j]:
#             # s[i],s[j]=s[j],s[i]
# print(s)

#             t=s[i]
#             s[i]=s[j]
#             s[j]=t
# print(s)

# a=input()
# s=[a]
# print(s)
# a=input()
# b=input()
# if 100<=a<b<=1000:
#     for i in range(a,b):
#         x=i/100
#         y=i%100/10
#         z=i%10
#         if i==x*x*x+y*y*y+z*z*z:
#             print(i)
# else:
#     print('输入值不合理')

# a=str(' ')
# s=[]
# print(a)



# a=input()
# b=input()
# c=input()
# if 1<=a<=10 and 1<=b<=10 and 1<=c<=10:
#     if a+b>c and a+c>b and b+c>a:
#         if a==b==c:
#             print('等边三角形')
#         else:
#             print('普通三角形')
#     else:
#         print('非三角形')
# else:
#     print('输入的值超出范围')


a=raw_input()
print(type(a))
s=int(a)
print(s)
for i in a:
    print(i)






