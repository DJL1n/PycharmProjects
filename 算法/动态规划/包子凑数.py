"""
作者：legionb
日期：2024年03月13日
"""
n=int(input())
long=[]
for i in range(n):
    long.append(int(input()))
dp=list(range(1,min(long)))
num=len(dp)
