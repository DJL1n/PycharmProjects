"""
作者：legionb
日期：2024年04月07日
"""
import copy

sumlist=[1,2,3,4,5]
difList=[0]*5
difList[0]=sumlist[0]
for i in range(1,5):
    difList[i]=sumlist[i]-sumlist[i-1]
print(difList)
difList[0]+=1
sumlist2=copy.deepcopy(difList)
for i in range(1,5):
    sumlist2[i]=sumlist2[i]+sumlist2[i-1]
print(sumlist2)