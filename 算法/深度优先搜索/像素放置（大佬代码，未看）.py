# """
# 作者：legionb
# 日期：2024年04月08日
# """
# def DFS(dotAddress):
#     for i in range(3):
#         for j in range(3):
#             chess[dotAddress[0]+dx[i]][dotAddress[1]+dy[i]]=1
#             DFS
# n,m=map(int,input().split())
# lst=[]
# for j in range(n):
#     lst.append([int(i) if '0'<=i<='9' else i for i in input()])
# record=[]
# for i in range(n):
#     for j in range(m):
#         if type(lst[i][j]) is int:
#             record.append([i,j])
# print(lst)
# chess=[[0]*m for i in range(n)]
# dx=[-1,0,1]
# dy=[-1,0,1]

import sys


def get(x, y):  # 获取一个位置附近的黑色网格数
    cnt = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            tx, ty = dx + x, dy + y
            if 1 <= tx < n + 1 and 1 <= ty < m + 1:
                if ans[tx][ty] == 1:
                    cnt += 1
    return cnt


def check(x, y):  # 判断一个位置附近的黑色网格数是否与地图中的相等
    if v[x][y] == -1: return True
    return v[x][y] == get(x, y)


def dfs(x, y):  # 装填网格，从左到右，从上到下，每次到九宫格右下角就判断
    if x == n + 1:  # 全部填满
        # 只测试最后一行,其余已测试过
        for j in range(1, m + 1):
            if not check(x - 1, j): return
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                print(ans[i][j], end='')
            print()
        sys.exit(0)

    if y == m:
        ans[x][y] = 0
        # 测试左上格以及上格
        if x > 1:  # 第一行不测
            if check(x - 1, y):
                if y > 1:  # 第一列不测左上
                    if check(x - 1, y - 1):
                        dfs(x + 1, 1)
                else:
                    dfs(x + 1, 1)
        else:
            dfs(x + 1, 1)
        # if not (x>1 and (check(x-1, y)==False or (y>1 and check(x-1, y-1)==False))): dfs(x+1, 1)
        ans[x][y] = 1
        if x > 1:
            if check(x - 1, y):
                if y > 1:
                    if check(x - 1, y - 1):
                        dfs(x + 1, 1)
                else:
                    dfs(x + 1, 1)
        else:
            dfs(x + 1, 1)
        # if not (x>1 and (check(x-1, y)==False or (y>1 and check(x-1, y-1)==False))): dfs(x+1, 1)
        return

    ans[x][y] = 0
    # 测试左上格
    if x > 1 and y > 1:  # 第一行或第一列不测左上
        if check(x - 1, y - 1): dfs(x, y + 1)
    else:
        dfs(x, y + 1)
    # if not (x>1 and y>1 and check(x-1, y-1)==False): dfs(x, y+1)
    ans[x][y] = 1
    if x > 1 and y > 1:
        if check(x - 1, y - 1): dfs(x, y + 1)
    else:
        dfs(x, y + 1)
    # if not (x>1 and y>1 and check(x-1, y-1)==False): dfs(x, y+1)


n, m = map(int, input().split())
v = [[0 for i in range(m + 1)] for j in range(n + 1)]
ans = [[0 for i in range(m + 1)] for j in range(n + 1)]
for i in range(1, n + 1):
    line = input()
    for j in range(1, m + 1):
        if line[j - 1] == '_':
            v[i][j] = -1
        else:
            v[i][j] = int(line[j - 1])

dfs(1, 1)