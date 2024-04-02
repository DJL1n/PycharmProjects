"""
作者：legionb
日期：2024年04月02日
"""
import numpy as np


def judge_linjie(i, j, m) -> bool:
    x1 = i // m
    y1 = i % m
    x2 = j // m
    y2 = j % m
    if lst[x1][y1] != 'E' or lst[x2][y2] != 'E':
        return False
    else:
        if x1 == x2:
            return abs(y1 - y2) == 1
        if y1 == y2:
            return abs(x1 - x2) == 1


n, m = map(int, input().split())
lst = [input() for i in range(n)]
print(lst)
total = n * m
linjie = [[0] * total for _ in range(total)]
for i in range(total):

    for j in range(i + 1, total):

        if i == j: continue

        if judge_linjie(i, j, m):
            linjie[i][j] = 1
            linjie[j][i] = 1
print(linjie)

A = np.array(linjie)

print(np.linalg.det(A[1:, 1:]))