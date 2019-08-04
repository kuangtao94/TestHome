from bs4 import BeautifulSoup
Teacher = open("./file.html","r",encoding='utf-8')
soap = BeautifulSoup(Teacher,"html.parser")
# prettify()可以自动解析为html格式
#print(soap.prettify())
print(type(soap))
tag = soap.title
print(type(tag)) # tag对象
string = tag.string # NavigableString对象
print(type(string))
comment = soap.b.string # Comment对象
print(type(comment))

tag1 = soap.head
print(type(tag1)) #返回的是tag标签的对象
print(tag1)
tag2 = soap.title
print(tag2)
#如果有多个相同的标签,返回第一个
tag3 = soap.a
print(tag3)
print(tag3.name)
#整个html对象的属性
print(soap.name)