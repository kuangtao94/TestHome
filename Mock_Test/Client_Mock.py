import requests
import shutil

def send_Mock(url):
    r = requests.get(url)
    return r.status_code

def visit_Mock():
    return send_Mock("http://www.Teacherketang.com/")

class Remove(object):
    def rmdir(self,path="E:/"):
        re = shutil.rmtree(path)
        if re == None:
            return "seccess"
        else:
            return "fail"

    def exists_get_rmdir(self):
        return self.rmdir()