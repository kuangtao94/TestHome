"""
1、根据字典key=values的值,对其ASCII码进行排序
    1、请求数据不明确
        *arg 元组，**kwargs 字典
    2、如何进行排序

2、把排序后的字典以字符串的形式进行拼接
    urllib库中的parse进行对字符串进行拼接
3、Md5加密
    hashlib 对数据进行加密
思路：
1、使用函数的动态函数来解决不明确的数据
2、使用内置函数 sorted()来对ASCII进行排序
3、使用urllib库中的parse进行对字典进行拼接处理
4、使用hashlib对字符串进行加密
"""
from urllib import parse
import hashlib
def datasign(*args,**kwargs):
    """先排序，后强制转换为字典"""
    dict1 = dict(sorted(kwargs.items(),key=lambda item:item[0]))
    dict2 = sorted(kwargs.items(), key=lambda item: item[0])
    """使用parse进行字典的拼接"""
    srt = parse.urlencode(dict1)
    """对MD5进行实例化"""
    md = hashlib.md5()
    md.update(srt.encode("utf=8"))
    print(srt,type(srt))
    print(dict2,type(dict2))
    return md.hexdigest()

dict3 = {"a":"a","name":"Tao","Adderss":"shenzhen","b":"b","c":"c"}
print(datasign(**dict3))