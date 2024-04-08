"""
作者：legionb
日期：2024年04月08日
"""
def ChildtreeSize(n,m,k):
    if k>n:
        return
    global count
    count+=1
    for i in range()

N=int(input())
lst=[0]+[1]*10**9
n=len(lst)
for i in range(1,n):
    lst[i]+=lst[i-1]
for i in range(N):
    count=0
    n,m,k=map(int,input().split())
    ChildtreeSize(n,m,k)