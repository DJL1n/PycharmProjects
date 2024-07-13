"""
作者：legionb
日期：2024年07月13日
"""


def find_root(x):
    while disjoint[x] >= 0:
        x = disjoint[x]
    return x


def conbine(x, y):
    disjoint[x] += disjoint[y]
    disjoint[y] = x


N, M, K = map(int, input().split())
cost = 0
disjoint = [-1] * N
graph = []
for i in range(M):
    X, Y, L = map(int, input().split())
    graph.append([X - 1, Y - 1, L])
graph.sort(key=lambda x: x[2])
# print(graph)
for edge in graph:
    x, y, c = edge

    x_root = find_root(x)
    y_root = find_root(y)
    # print(x_root,y_root)
    # print(graph)
    if x_root == y_root:
        continue
    else:
        conbine(x_root, y_root)

    cost += c
    N -= 1
    if N == K:
        print(cost)
        break
