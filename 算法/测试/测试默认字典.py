"""
作者：legionb
日期：2024年04月10日
"""
import collections

s='caabdc'
dic1=collections.defaultdict(int)
for i in s:
    dic1[i]+=1
print(dic1)