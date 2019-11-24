# 字典 Dictionary

"""dic = {"k":12,"v":23,"d":34,"t":45,"y":56}
print("nimi:",dic["d"])


dict1 = dict((("k",12),("v",23),("d",34),("t",45),("y",56)))

dict2 = dict(k = 12,v = 23,d = 34,t = 45,y = 56)

dict3 = dict([("k",12),("v",23),("d",34),("t",45),("y",56)])

dict4 = {"k":12,"v":23,"d":34,"t":45,"y":56}



a = {"one":1,"two":2,"three":3}
b = dict(one = 1,two = 2,three = 3)
c = dict({"one":1,"two":2,"three":3})
d = dict({("one",1),("two",2),("three",3)})
e = dict(zip(["one","two","three"],[1,2,3]))
a == b == c == d == e


"""
print("="*12,"学员管理系统","="*14)
print("{0:1} {1:13} {2:15}".format(" ","1.查看学员信息","2.添加学员信息"))
print("{0:1} {1:13} {2:15}".format(" ","3.删除学员信息","4.退出系统"))

print("  ","1.查看学员信息","  ","2.添加学员信息")
print("  ","3.删除学员信息","  ","4.退出系统")

print("="*40)

# Dictionnary 内置方法

"""dict = {}
dict.fromkeys((1,2,3))"""

def test(** parames):
    print("有%d个参数" %len(parames))
    print("它们分别是：",parames)

test(a = 1,b = 2,c = 3,d = 4,e = 5)

a = {"one":1,"two":2,"three":3}
test(** a)


def test(* parames):
    print("有%d个参数" %len(parames))
    print("它们分别是：",parames)

b = (1,2,3,4)
test(* b)

c = ["one","two","three","four","five","six"]
test(* c)
