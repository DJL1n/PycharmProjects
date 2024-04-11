"""
作者：legionb
日期：2024年04月11日
"""
N=int(input())
m1=float("inf")
lst=[]
for i in range(N):
    O,X=map(int,input().split())
    m1=min(m1,O//X)
    lst.append([O,X])
m2=m1
con=True
while con:
    m2 -= 1
    for i in range(N):
        if lst[i][0]//m2!=lst[i][1]:
            con=False
            break



print(m2+1,m1)