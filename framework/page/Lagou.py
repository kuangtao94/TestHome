import json
from unitcase.public import *
from unitcase.oprationjson import OprationJson
from unitcase.oprationExcel import OprationExcel

operationJson = OprationJson()
operationExcel = OprationExcel()

def setSo(kd =None):
    """对搜索的数据重新赋值"""
    dict1 = json.loads(operationJson.getRequestDats(1))
    dict1["kd"] = kd
    return dict1
#print(setSo("xin"))
def setPositonId():
    dict1 = json.loads(operationJson.getRequestDats(2))
    dict1["positonId"] = ""

def writePositionId(content):
    """把职位的ID号写入到文件当中"""
    with open(get_dir(filename="positionId"),"r") as file:
        file.write(content)



#print(setSo("性能测试工程师"))