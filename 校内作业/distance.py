"""
作者：legionb
日期：2024年06月13日
"""
from collections import deque
def distance(adj_list:list,s:int)->list:
    n=len(adj_list)
    distances=[float("inf")]*n
    distances[s]=0
    q=deque()
    q.append(s)
    visited=set()
    while q:
        cur=q.popleft()
        if cur not in visited:
            visited.add(cur)
            for i in adj_list[cur]:
                if i not in visited:
                    distances[i]=min(distances[cur]+1,distances[i])
                    q.append(i)
    return distances

adj_list = [[], [2, 3], [1, 4], [1], [2]]
d = distance(adj_list, 0)
print(d)
d = distance(adj_list, 2)
print(d)