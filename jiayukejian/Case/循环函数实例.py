sum = 0
for x in range(101):
    sum = sum + x
print(sum)
     # range(5)生成的序列是从0开始小于5的整数：
list(range(5))
[0, 1, 2, 3, 4]

sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
    print(sum)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print("Hello",x)
    #sum=0
    #while sum<3:
     #   print("Hello",L[sum])
     #   sum+=1


names = ['Michael', 'Bob', 'Tracy']  #  for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
for name in names:
    print(name)

sum = 0     #  计算1-10的整数之和，可以用一个sum变量做累加：
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:    #进入死循环时用 ctrl+C 来强制执行
    n = n + 1
    if n % 2 == 1: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

#  break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。