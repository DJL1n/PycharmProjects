import os
import sys

# 请在此输入您的代码
# 实现 Dijkstra 算法
import heapq

n, m = map(int, input().split())  # 节点数量和边数量
distance = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    distance[u].append((v, w))

dp = [sys.maxsize] * (n + 1)
# 创建列表存储从起点到每个节点的最短距离。初始时，将每个节点的距离设置为无穷大
q = []  # 空堆
heapq.heappush(q, (0, 1))  # 起点 1 加入堆中，初始距离为 0
dp[1] = 0


def dijkstra():
    visit = [0] * (n + 1)
    while q:
        v = heapq.heappop(q)[1]
        if visit[v] == 1:
            continue
        visit[v] = 1
        for a, b in distance[v]:
            if visit[a] == 1:
                continue
            dp[a] = min(dp[a], dp[v] + b)
            heapq.heappush(q, (dp[a], a))


dijkstra()  # 调用算法

print(0, end=" ")

for i in range(2, n + 1):
    # 输出从起点到其他节点的最短距离，如果某个节点不可达，则输出 -1
    if dp[i] == sys.maxsize:
        print(-1, end=" ")
    else:
        print(dp[i], end=" ")
