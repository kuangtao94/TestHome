"""
根据字符串的形式去查找某个模块中寻找的XX函数 --> getattr()
根据字符串的形式去某个模块中判断东西是否存在 --> hasattr()
根据字符串的形式去某个模块中设置东西 --> setattr()
根据字符串的形式去某个模块中删除东西 --> delattr()

"""
# import login
# obj = login.Person()
# if hasattr(obj,"info"): #判断字符串是否存在
#     f = getattr(obj,"info")
#     f()
# else:
#     print("Sorry")

# f = setattr(obj,"exit","This is exit method")
# f1 = hasattr(obj,"exit")
# print("setattr后的结果：",f1)
# f = getattr(login,"str")
# print(f)
# f1 = delattr(login,"str")
# print(f1)
# f2 = hasattr(login,"str")
# print(f2)

#在login模块中设置变量str1
# f = setattr(obj,"str1","Hello World")
# #判断str2是否存在
# f1 = hasattr(obj,"str1")
# print(f1)
#
# #在login模块中删除str
# f2 = hasattr(login,"str")
# print("未删除str的结果：",f2)
# f3 = delattr(login,"str")
# f4 = hasattr(login,"str")
# print("删除str的结果：",f4)

# url = input("请输入路由地址：\n")
# target_models,target_function = url.split("/")
# m = __import__(target_models)
# #判断m模块中是否存在target_function
# if hasattr(m,target_function):
#     #查看m模块中寻找存在target_function
#     target_function = getattr(m,target_function)
#     target_function()
# else:
#     print("Not find 404 Page")


