from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.cnblogs.com/Teachertao/")
#爬糗事百科首页的段子
# r = requests.get("https://www.qiushibaike.com/")
# qiushi = r.content
# #print(qiushi)
# soup = BeautifulSoup(qiushi,"html.parser")
# #print(soup)
# duanzi = soup.find_all(class_="recmd-right")
# #print(duanzi)
# db = [item for item in duanzi]
# print(db)

# 请求首页后获取整个 html 界面
blog = r.content
#print(blog)
#用html.parser解析出html
soup = BeautifulSoup(blog,"html.parser")
#print(soup.prettify())
#获取所有的class属性为"block_title"，返回Tag类
time = soup.find_all(class_="block_title")
#print(time)

db = [item for item in time]
#print(db)
# 获取title
title = soup.find_all(class_="posttitle")
#print(title)
#获取摘要
desc = soup.find_all(class_="c_b_p_desc")
# len 函数获取子节点的个数
#print(len(desc))
# 循环打印出子节点
# try:
#     for item in desc:
#         print(item)
# except:
#     pass
# else:
#     print(desc[0])
# finally:
#     pass

# for item in desc:
# # tag 的 .contents 属性可以将 tag 的子节点以列表的方式输出
#     print(item)
#children生成list对象
#print(desc.children)

tag_soup = soup.find(class_="catListTitle")
print(tag_soup)
ui_tag = soup.find_all("a")
print(ui_tag)
for item in soup:
    print(item.string)