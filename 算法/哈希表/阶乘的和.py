"""
作者：legionb
日期：2024年04月03日
"""
from collections import defaultdict
n=int(input())
A=[int(i) for i in input().split()]
A.sort()
m=A[0]
dic1=defaultdict(int)
for i in A:
    dic1[i]+=1
while dic1[m]%(m+1)==0:
    m+=1
    dic1[m]+=dic1[m-1]//m
print(m)
