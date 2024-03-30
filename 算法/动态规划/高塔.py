"""
作者：legionb
日期：2024年03月11日
"""
data=[int(_) for _ in input().split()]
n=data[0]
m=data[1]
A=[int(_) for _ in input().split()]
dp=[0]*n
for i in range(n):
    