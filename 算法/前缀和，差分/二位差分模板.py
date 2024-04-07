"""
作者：legionb
日期：2024年04月07日
"""


def change(x1, y1, x2, y2, x):
    changeList[x1][y1] += x
    changeList[x2 + 1][y2 + 1] += x
    changeList[x2 + 1][y1] -= x
    changeList[x1][y2 + 1] -= x
    # print(changeList)


n, m, q = map(int, input().split())
lst = [[0] * (m + 1)]
for i in range(n):
    lst.append([0] + [int(j) for j in input().split()])
changeList = [[0] * (1000) for i in range(1000)]
for k in range(q):
    x1, y1, x2, y2, x = map(int, input().split())
    change(x1, y1, x2, y2, x)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        changeList[i][j] += changeList[i - 1][j] + changeList[i][j - 1] - changeList[i - 1][j - 1]
        lst[i][j] += changeList[i][j]
print(lst)
