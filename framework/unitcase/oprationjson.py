from unitcase.public import *
from unitcase.oprationExcel import OprationExcel
import json

class OprationJson:
    def __init__(self):
        """对OprationExcel进行实例化，其实所有的类都有构造函数"""
        self.excel = OprationExcel()

    def getReadJson(self):
        with open(get_dir("data","OprationJson.json"),encoding="utf-8") as fp:
             return json.load(fp)

    def getRequestDatas(self,row):
        """引用data.xls表格，提取参数"""
        #return type(self.getReadJson())
        #return self.getReadJson()[self.excel.getDate(row)]
        """字典的序列化"""
        return json.dumps(self.getReadJson()[self.excel.getDate(row)])


# opp = OprationJson()
# print(opp.getRequestDats(1),type(opp.getRequestDats(1)))