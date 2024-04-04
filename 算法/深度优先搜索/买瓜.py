"""
作者：legionb
日期：2024年04月04日
"""


def dfs(i, weight, cut):
    global res
    if cut >= res:
        return
    if weight == m:
        res = min(cut, res)
        return
    if i == n or weight > m or B[i] < m - weight:
        return
    dfs(i + 1, weight, cut)
    dfs(i + 1, weight + A[i] / 2, cut + 1)
    dfs(i + 1, weight + A[i], cut)


n, m = map(int, input().split())
A = [int(i) for i in input().split()]

res = n + 1
A.sort(reverse=True)
# print(A)
B = []
for i in range(n):
    B.append(sum(A[i:]))
# print(B)
dfs(0, 0, 0)
print(res if res != n + 1 else -1)