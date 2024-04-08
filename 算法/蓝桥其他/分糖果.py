"""
作者：legionb
日期：2024年04月08日
"""
import collections

n,x=map(int,input().split())
deliver=['']*x
sweet=collections.defaultdict(int)
for i in input():
    sweet[i]+=1
lst=sorted(sweet.items(),