"""
正则表达式
第一个参数是正则表达式模式，需要用原始字符来写"r"
第二个为查找的字符串，找到后返回的范围以下标为0，找不到则返回NONE
"""
# import re
# re.search(r"FishC","I Love FishC.com")
# #通配符 .
# re.search(r".","I Love FishC.com")
# #反斜杠 . 转义 查找 . 特殊元组
# re.search(r"\.","I Love FishC.com")
# #反斜杠加上小写字母d 匹配数字
# re.search(r"\d","I Love 3123 FishC.com")
# re.search(r"\d\d\d\d","I Love 3123 FishC.com")
# #中括号匹配里面的字符 或者匹配数字的范围
# re.search(r"[a - z]","I Love 3123 FishC.com")
# re.search(r"[0-2][0-5][0-5]","I Love 3123 FishC.com")
# #重复匹配的功能，数字5代表5个b {5,10}指b的范围，用大括号
# re.search(r"ab{5}c","abbbbbbbbc")
# re.search(r"ab{5,10}c","abbbbbbbbc")
# #匹配IP地址实例
# re.search(r"(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])","192.168.1.1")