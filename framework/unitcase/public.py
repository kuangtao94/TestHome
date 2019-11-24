import os

def get_dir(data=None,filename=None):
    """查找文件的路径"""
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,filename)
    #return os.path.join(os.path.dirname(os.path.dirname(__file__)))
    #return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,filename)

