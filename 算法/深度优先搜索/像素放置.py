"""
作者：legionb
日期：2024年04月08日
"""
n,m=map(int,input().split())
lst=[]
for j in range(n):
    lst.append([int(i) if '0'<=i<='9' else i for i in input()])
print(lst)
chess=[[0]*m for i in range(n)]
