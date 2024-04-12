"""
作者：legion
日期：2024年04月12日
"""
from collections import defaultdict
import heapq


def dijkstra():
    distances = [[10**6]*N for i in range(N)]
    distances[0][0] = 0
    priority_queue = [(0, 0)]
    while priority_queue:
        cur_v, cur_dist = heapq.heappop(priority_queue)
        # print(cur_v)
        # print(graph)
        for neighbor, weight in graph[cur_v].items():
            flag=False

            if distances[cur_v][0] + weight < distances[neighbor][0]:
                distances[neighbor][0] = distances[cur_v][0]+weight
                flag=True
            if distances[cur_v][K]+weight<distances[neighbor][K]:
                flag=True
                distances[neighbor][K]=distances[cur_v][K]+weight

            for j in range(1,K+1):
                if distances[neighbor][j]>distances[cur_v][j-1]:
                    flag=True
                    distances[neighbor][j]=distances[cur_v][j-1]
            if flag is True:
                heapq.heappush(priority_queue,(neighbor,distances[neighbor][0]))
    # print(distances)
    print(min(distances[N-1][0],distances[N-1][K]))


N, K, M = map(int, input().split())
graph = {}
for i in range(M):
    u, v, w = map(int, input().split())
    if u not in graph:
        graph[u]={}
    if v not in graph:
        graph[v]={}
    graph[u][v]=w
    graph[v][u]=w
# print(graph)
dijkstra()

