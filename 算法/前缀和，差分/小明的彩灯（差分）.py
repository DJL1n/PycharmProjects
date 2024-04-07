"""
作者：legionb
日期：2024年04月07日
"""


def get_difference_list(lst: list) -> list:
    lst1 = [lst[0]]
    for i in range(1, N):
        lst1.append(lst[i] - lst[i - 1])
    return lst1


def change(l, r, x):
    dif[l] += x  # 这里就是差分的精髓，用O（1）的时间复杂度代替O（m）
    if r + 1 < N:
        dif[r + 1] -= x


def getBack():
    for i in range(1, N):
        dif[i] = dif[i] + dif[i - 1]
    print(' '.join(str(max(dif[i], 0)) for i in range(N)))


N, Q = map(int, input().split())
lst = [int(i) for i in input().split()]
dif = get_difference_list(lst)
# print(dif)
for i in range(Q):
    l, r, x = map(int, input().split())
    change(l - 1, r - 1, x)
getBack()

# N, Q = map(int, input().split())
# a = list(map(int, input().split()))
# op = [0 for _ in range(N+1)]
# for _ in range(Q):
#   l, r, x = map(int, input().split())
#   op[l-1] += x
#   op[r] -= x
#
# for i in range(1, N):
#   op[i]+= op[i-1]
# print(' '.join(str(max(a[i] + op[i], 0)) for i in range(N)))
# 大佬的思路，虽然都是先差分再求和回去，但是只需要记录变化量就好，没必要一开始直接化到差分列表。简单说就是得到变化差分列表，将变化量再一起带到原列表中
