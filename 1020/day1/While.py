
# *** Settings ***
# Library           Selenium2Library
#
# *** Test Cases ***
# test01
#     [Documentation]    测试淘宝
#     Open Browser    https://login.taobao.com/member/login.jhtml    chrome
#     Click Element    xpath=//*[@id="J_Quick2Static"]
#     Sleep    1
#     Input Text    xpath=//*[@id="TPL_username_1"]    123
#     Input Text    xpath=//*[@id="TPL_password_1"]    123
#     ${title_1}    Get Title
#     Click Button     xpath=//*[@id="J_SubmitStatic"]
#     Sleep     2
#     ${title_2}    Get Title
#     should not contain    ${title_2}    ${title_1}
#     Close browser


'''count = 0
while (count < 9):
    print("This count is :", count)
    count += 1
print("Good bye!")'''

numbers = [12, 34, 42, 5, 8, 9]
even = []
odd = []
while (len(numbers)) > 0:
    number = numbers.pop()
    if (number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)

i = 1
while i < 10 :
    i += 1
    if i % 2 > 0 :
        continue
    print (i)

a = 1
while 1 :
    print (a)
    a += 1
    if a > 10 :
        break
"""var = 1
while var == 1 :
    num = raw_input("Enter a number :")
    print("You entered :", num)
print("Good bye!")"""


count = 0
while count < 5 :
    print(count,"is less than 5")
    count += 1
else :
    print(count,"is not less than 5")

# while 死循环
flag = 1
while (flag != 1) :
    print("Given flag is really true")
    print("Good bye")


for num in  range(10,20):
    for i in range(2,num):
        if num % i == 0 :
            j = num / i
            print("%d 等于 %d * %d "%(num,i,j))
            break
else:
    print (num,"是一个质数")

for i in range(1,10):
    for k in range(1,i+1):
        m = k * i
        print ("%d * %d = %d\t"%(k,i,m)),        print("\n")




i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j):
            break
        j = j + 1
    if (j > i / j):
        print(i,"是素数")
    i += 1
print("Good bye")




rows = int(raw_input("输入行数"))
for i in range(0,rows):
    for k in range(0,2*rows -1):
        if(i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
            print("*")
        elif (i == rows -1) :
            if k % 2 == 0 :
                print("*")
            else:
                print("  ")
        else :
            print("  ")
    print(" \n ")

seore = int(input("请输入分数："))
if 100 > seore >= 90 :
    print("A")
elif 90 > seore >= 80 :
    print("B")
elif 80 > seore >= 60 :
    print("C")
elif  seore < 60 :
    print("D")
else  :
    print("输入错误")




