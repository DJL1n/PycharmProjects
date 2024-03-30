"""
作者：legionb
日期：2024年03月14日
"""
# NP完全问题

n,m=map(int,input().split())
speed=list(map(int,input().split()))
speed.sort(reverse=True)
mintime=[0]*m

for s in speed:
    min_index=mintime.index(min(mintime))
    mintime[min_index]+=s
max_time=max(mintime)
print(max_time)