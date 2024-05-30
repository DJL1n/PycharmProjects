"""
作者：legionb
日期：2024年05月27日
"""
from collections import deque;

def find_max(i):
    max_node=i
    visited=set()
    q=deque()
    q.append(i)
    while not q:
        cur=q.popleft()
        max_node=max(max(graph[cur]),max_node)
        print(max_node)
        for node in graph[cur]:
            q.append(cur)
    return max_node




N,M=map(int,input().split())
graph={}
for i in range(M):
    u,v=map(int,input().split())
    if u not in graph:
        graph[u]=[]
    graph[u].append(v)

res=[]
for i in range(1,N+1):
    res.append(find_max(i))
print(*res)