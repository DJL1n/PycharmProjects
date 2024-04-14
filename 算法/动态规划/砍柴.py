"""
作者：legionb
日期：2024年04月13日
"""
import math


def give_zhishu():
    lst = []
    for i in range(2, 100000):
        flag = True
        for j in range(2, int(math.sqrt(i))):
            if i % j == 0:
                flag = False
            break
        if flag is True:
            lst.append(i)
    return lst

def all_conditions(end):
    for i in range(10,end+1):


T = int(input())

lst = give_zhishu()
q = []
for i in range(T):
    q.append(int(input()))
end=max(q)
conditions=[0,1,2,3,4,5,6,7,8,9]
who_win=[0,0,1,1,1,1,1,0,1,0]
if end>9:
    all_conditions(end)