"""
作者：legionb
日期：2024年02月25日
"""
def fullbag(w:int, W:list, V:list)->int:
    n=len(W)
    dp=[[0]*w for _ in range(n)]
    for i in range(n):
        for j in range(w):
