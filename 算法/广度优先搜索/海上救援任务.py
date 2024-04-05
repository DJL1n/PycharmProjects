"""
作者：legionb
日期：2024年04月05日
"""

# 广度优先算法在每一个点的第一次遍历都是到这个点最短的
# 像这种判断可不可以连接的，一定要避免重复，不然循环不会停止

import queue

n, m = map(int, input().split())
lst = [list(map(int, list(input()))) for _ in range(n)]
# print(lst)
K = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(K):
    x1, y1, x2, y2 = map(int, input().split())

    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1

    target = [x2, y2]
    records = queue.Queue()
    records.put([x1, y1, 0])
    repeat = {str([x1, y1])}

    while not records.empty():
        # print(1)
        record = records.get()
        if record[:2] == target:
            print(record[-1])
            break
        x0, y0 = record[:2]

        for j in range(4):
            if -1 < x0 + dx[j] < n and -1 < y0 + dy[j] < m and lst[x0 + dx[j]][y0 + dy[j]] == 1 and str(
                    [x0 + dx[j], y0 + dy[j]]) not in repeat:
                repeat.add(str([x0 + dx[j], y0 + dy[j]]))
                records.put([x0 + dx[j], y0 + dy[j], record[-1] + 1])
                # print([x0+dx[j],y0+dy[j],record[-1]+1])

    else:
        print("Impossible")
