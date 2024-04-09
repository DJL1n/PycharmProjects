"""
作者：legionb
日期：2024年04月09日
"""
import collections

n=int(input())
dic1=collections.defaultdict(int)
standard=n//10
lst=[]
expense=0
for i in range(n):
    a,b=map(int,input().split())#第一行是值，第二行代价
    dic1[a]+=1
    lst.append([a,b])
lst=sorted(lst,key=lambda x:x[1])
for i in range(n):
    if dic1[lst[i][0]]>standard:
        expense+=lst[i][1]
        dic1[lst[i][0]]-=1
print(expense)


