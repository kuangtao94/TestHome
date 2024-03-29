# 汉诺塔思想笔记
# 认识汉诺塔的目标：把A柱子上的N个盘子移动到C柱子
# 递归的思想就是把这个目标分解成三个子目标
# 子目标1：将前n-1个盘子从a移动到b上
# 子目标2：将最底下的最后一个盘子从a移动到c上
# 子目标3：将b上的n-1个盘子移动到c上
# 然后每个子目标又是一次独立的汉诺塔游戏，也就可以继续分解目标直到N为1
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b)# 子目标1
        move(1, a, b, c)# 子目标2
        move(n-1, b, a, c)# 子目标3
n = input('enter the number:')
move(int(n), 'A', 'B', 'C')

print
import base64

def safe_base64_decode(s):
    if isinstance(s, str):
        s += (4 - len(s) % 4) # '='
        return base64.b64decode(s)
    else:
        s += (4 - len(s) % 4) # b'='
        return base64.b64decode(s)