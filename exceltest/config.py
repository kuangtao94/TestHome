import configparser
import os
import sys


# def base_file(filename = None):
#     return os.path.join(os.path.dirname(__file__),filename)

#实例化变量
config = configparser.ConfigParser()

#写入数据内容到config中

def set_sort(sql="data",linux="Linux",de="Demand"):
    config.add_section(sql)
    config.set(sql,"IP","127.0.0.1")
    config.set(sql,"PORT","3306")
    config.set(sql,"USERNAME","root")
    config.set(sql,"PASSWORD","root")

    config.add_section(linux)
    config.set(linux,"IP", "192.168.2.1")
    config.set(linux, "PORT", "20")
    config.set(linux, "USERNAME", "root")
    config.set(linux, "PASSWORD", "rqfa32134")

    config.add_section(de)
    config.set(de,"sex","男女不限")
    config.set(de,"degree","本科以上")
    config.set(de,"major","计算机相关")

    config.write(sys.stdout)
    config.write(open("config.txt","w"))

    #return set_sort(sql="data",linux="Linux",de="Demand")

#读取配置文件,并赋予给config
config.read("./config.txt")
print(config.get("data","PORT"))













