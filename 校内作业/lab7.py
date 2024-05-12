"""
作者：legionb
日期：2024年05月11日
"""
from collections import deque
import heapq

def BFS(adj_list, start):
    n = len(adj_list)
    Dist = [-1] * n
    pre = [-1] * n
    q = [(start, 0)]
    min_girth = float("inf")

    while q:
        cur, dist = heapq.heappop(q)
        for next in adj_list[cur]:
            if Dist[next] != -1:
                if pre[cur] != next :
                    print(start,cur,dist,next,pre[cur])
                    min_girth = min(min_girth, Dist[next] + 1 + dist)

            else:
                Dist[next] = dist + 1
                pre[next] = cur
                heapq.heappush(q,(next,dist+1))
    return min_girth


def find_girth(adj_list):
    size = len(adj_list)
    min_girth = float("inf")
    for i in range(size):
        min_girth = min(min_girth, BFS(adj_list, i))
    return "inf" if min_girth == float("inf") else min_girth


adj_list = [[2],[3],[0,3],[1,2,4,5],[3],[3]]
print(find_girth(adj_list))
