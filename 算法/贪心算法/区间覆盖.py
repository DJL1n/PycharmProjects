"""
作者：legionb
日期：2024年03月16日
"""
import math
def cmp(leida,dao,d):
    if (leida-dao[0])**2+dao[1]**2>d**2:
        return True
    return False
n,d=map(int,input().split())
island=[]
for i in range(n):
    island.append(tuple(map(int,input().split())))
island=sorted(island,key=lambda x:x[0])
lada=[]
for j in island:
    if lada == [] or cmp(lada[-1],j,d):
        dis=math.sqrt(d**2-j[1]**2)
        lada.append(j[0]+dis)
print(len(lada))