#coding:utf-8
#操作文本文档
#读文档
# fp=open('user.txt')         #打开文档
# # print(fp.readlines())        #读取文档，将读取的内容保存为列表
# print(fp.read())
# fp.close()

# with open('user.txt') as fp:
#     print(fp.readlines())

with open('user.txt','a') as fp:                #以写入的方式打开文档，当文件不存在时，会创建该文件
    for i in range(1,10):
        for j in range(1,i+1):
            fp.writelines('%dx%d=%d\t'%(j,i,i*j))
        fp.writelines('\n')