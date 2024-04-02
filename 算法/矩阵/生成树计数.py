"""
作者：legionb
日期：2024年04月02日
"""
import numpy as np


def judge_linjie(i, j) -> bool:
    x1 = i // m
    y1 = i % m
    x2 = j // m
    y2 = j % m
    if lst[x1][y1] != 'E' or lst[x2][y2] != 'E':
        return False
    else:
        if x1 == x2 and y2 == y1:
            return False
        if x1 == x2:
            return abs(y1 - y2) == 1
        if y1 == y2:
            return abs(x1 - x2) == 1


n, m = map(int, input().split())
lst = [input().split() for i in range(n)]
total = n * m
linjie = [[0] * total for _ in range(total)]
for i in range(total):
    for j in range(total):
        if judge_linjie(i, j):
            linjie[i][j] = 1

A = np.array(linjie)
D = np.diag(np.sum(A, axis=1))
L = D - A
print(np.linalg.det(L[1:.1:]) % (10 ** 9 + 7))
