"""
作者：legionb
日期：2024年04月07日
"""

lst=[1,2,3,4,5,6,7]
for i in range(1,len(lst)):
    lst[i]=lst[i]+lst[i-1]
print(lst)
# l,r=map(int,input().split())
l,r=2,4
print(lst[r]-lst[l-1])