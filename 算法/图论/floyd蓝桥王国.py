"""
作者：legionb
日期：2024年05月31日
"""
import os
import sys

# 请在此输入您的代码
N, M, Q = map(int, input().split())
weight = [[0 if i == j else sys.maxsize for i in range(N + 1) ] for j in range(N + 1)]  # 领接矩阵
for i in range(M):
    u, v, w = map(int, input().split())
    weight[u][v] = min(weight[u][v], w)
    weight[v][u] = weight[u][v]
for k in range(1, N + 1):  # N次递推
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):  # 更新最小值
                weight[i][j] = min(weight[i][j], weight[i][k] + weight[k][j])
                weight[j][i] = weight[i][j]

for i in range(Q):
    st, ed = map(int, input().split())
    t = weight[st][ed]
    if t == sys.maxsize:
        print(-1)
    else:
        print(t)