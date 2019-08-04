import xml.dom.minidom
import os

# def file_path():
#     return os.path.join("D:\Test\TestCase","ddd.xml")
# #print(file_path())
# file_path()
def getXml(value=None):
    '''获取单节点的数据内容'''
    xmlfile = xml.dom.minidom.parse("ddd.xml")
    db = xmlfile.documentElement
    itemlist = db.getElementsByTagName("yan")
    item = itemlist[0]
    return item.firstChild.data
#print(getXml(value="yan"))
getXml()
def getBat(parser=None,sanme=None):
    '''获取节点的数据内容'''
    xmlfile = xml.dom.minidom.parse("ddd.xml")
    db = xmlfile.documentElement
    itemlist = db.getElementsByTagName(parser)
    item = itemlist[0]
    return item.getAttribute(sanme)

print(getBat("WuYA","address"))

