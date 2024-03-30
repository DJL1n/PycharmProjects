def judge(x, y, n, north, west):
    if n > x > -1 and n > y > -1 and north[x] != 0 and west[y] != 0:
        return True
    return False

def find(n, north, west, result):
    if north == [0] * n and west == [0] * n and result[-1] == n ** 2 - 1:
        path = [str(i[0] + n * i[1]) for i in result]
        print(' '.join(path))
        return

    x, y = result[-1]
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        if judge(x + dx, y + dy, n, north, west):
            north[x + dx] -= 1
            west[y + dy] -= 1
            result.append((x + dx, y + dy))

            find(n, north, west, result)

            north[x + dx] += 1
            west[y + dy] += 1
            result.pop()

# 初始化result为起始位置
N=int(input())
north=[int(i) for i in input().split()]
west=[int(i) for i in input().split()]
result = [(0, 0)]
north[0] -= 1
west[0] -= 1
find(N, north, west, result)
