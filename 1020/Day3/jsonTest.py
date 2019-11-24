#!/usr/bin/env python
#-*- conding:utf-8 -*-
# Teacher Tao

import json
import requests
"""文件的序列化与反序列化"""
r = requests.post(url = "http://www.weather.com.cn/data/sk/101190408.html")
print(r.text)
print(r.content.decode("utf-8"))
#对文件进行序列化 --> 就是把服务端响应数据写入到文件中
json.dump(r.content,open("weather.json","r"))

#文件的反序列化:就是读取文件中的内容
"""
1.文件的反序列化后，类型是unicode
2.进行编码，把Unicode类型转换为str
3.然后再进行反序列化，把str类型转换为字典类型
"""
dict1 = json.loads((json.load(open("weather.json","r"))).encode("utf-8"))
print(dict,type(dict))



"""
序列化：把python数据类型转换为str字符串类型 用dumps
反序列化：把str字符串类型转化为python数据结构 用 loads
"""
"""字典的序列化与反序列化的过程"""
dict = {"name":"Teacher","age":18}
"""序列化 dict --> str"""
dict_str = json.dumps(dict)
print("序列化后的结果信息：",dict_str,type(dict_str))

"""反序列化 str --> dict"""
str_dict = json.loads(dict_str)
print("反序列化后的结果信息：",str_dict,type(str_dict))

"""列表的序列化与反序列化的过程"""
list = ["admin","age","address"]

"""序列化 list --> str"""
list_str = json.dumps(list)
print("序列化后的结果信息：",list_str,type(list_str))

"""反序列化 str --> list """
str_list = json.loads(list_str)
print("反序列化后的结果信息：",str_list,type(str_list))

"""元组的序列化与反序列化的过程"""
tuple = (1,2,3,5,6)

"""序列化 tuple --> str"""
tuple_str = json.dumps(tuple)
print("序列化后的结果信息：",tuple_str,type(tuple_str))

"""反序列化 str --> tuple """
str_tuple = json.loads(tuple_str)
print("反序列化后的结果信息：",str_tuple,type(str_tuple))