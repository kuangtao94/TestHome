"""
1、将小甲鱼的对话单独保存为boy_*.txt的文件(去掉"小甲鱼：")
2、将小客服的对话单独保存为boy_*.txt的文件(去掉"小客服：")
3、文件中总共有三段对话，分别保存为boy_1.txt、girl_1.txt、boy_2.txt、girl_2.txt
、boy_3.txt、girl_3.txt共6个文件！
"""
def save_file(boy,girl,count):

    file_name_boy = "boy_" + str(count) + ".txt"
    file_name_girl = "girl_" + str(count) + ".txt"

    boy_file = open("file_name_boy","w")
    gilr_file = open("file_name_girl","w")

    boy_file.writelines(boy)
    girl_file.writelines(girl)

    boy_file.close()
    girl_file.close()

def split_file(file_name):
    
    f = open(r"D:\Program Files\python36\test.txt")
    
    boy = [] # 定义参数
    girl = [] # 定义参数
    count = 1 # 保存为 1 2 3
    
#每次在打开文件中获取一行，迭代循环!
    for each_line in f:
    #如果对话的前 不等于 ==
        if each_line[:6] != "====":
        # 进行对each_line 进行分割以：开始分割，列表或字符串的方法调用
        # #每行按照：分割成1+1个子字符串，分别赋值给=前面的对象
            (role,line_spoken) = each_line.split(":",1)
            if role == "小甲鱼":
            #把小甲鱼说的话迭代在boy列表中
                boy.append(line_spoken)
            if role == "小客服":
            #把小客服说的话迭代在girl列表中
                girl.append(line_spoken)
        else:
            save_file(boy,girl,count)
                
            boy = []
            girl = []
            count += 1
        
    save_file(boy,girl,count)
    
    f.close()
    
split_file(r"D:\Program Files\python36\test.txt")

