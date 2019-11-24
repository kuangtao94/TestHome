from unitcase.oprationExcel import *
from unitcase.oprationjson import *
import requests

class Model:
    def __init__(self):
        self.operation = OprationJson()
        self.excel = OprationExcel()

    def post(self,row):
        try:
            r = requests.post(
                url=self.excel.getUrl(row=row),
                data=self.operation.getRequestDats(row=row),
                headers=self.excel.getHeaders(),
                timeout=6)
            return r
        except Exception as e:
            raise RecursionError("接口请求发生未知错误")

    def post1(self,row,data):
        try:
            r = requests.post(
                url=self.excel.getUrl(row=row),
                data=data,
                headers=self.excel.getHeaders(),
                timeout=6)
            return r
        except Exception as e:
            raise RecursionError("接口请求发生未知错误")

class IsAssces:
    def __init__(self):
        self.excel = OprationExcel()
    def isText(self,row,str2):
        flag = None
        if self.excel.getExpect(row) in str2:
            flag = True
        else:
            flag = False
        return flag



