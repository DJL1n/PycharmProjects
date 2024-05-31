"""
作者：legionb
日期：2024年05月30日
"""
from collections import deque

def top_sort():
    q=deque([u for u in graph if in_degree[u] == 0])
    count=0
    record=[0]*N
    while q:
        cur=q.popleft()
        count+=1

        record[cur-1]=count

        for val in graph[cur]:
            in_degree[val]-=1
            if in_degree[val]==0:
                q.append(val)
    return record

N,M=map(int,input().split())
graph={u:[] for u in range(1,N+1)}
for i in range(M):
    x,y=map(int,input().split())
    # if x not in graph:
    #     graph[x]=[]
    graph[x].append(y)
in_degree = {u: 0 for u in graph}
for key in graph:
    for value in graph[key]:
        in_degree[value] += 1

res=top_sort()
for i in range(N):
    print(res[i])
