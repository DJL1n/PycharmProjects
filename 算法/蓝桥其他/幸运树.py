"""
作者：legionb
日期：2024年04月03日
"""
# count = 0
# for i in range(10, 100000000):
#     n = len(str(i))
#     if n % 2 != 0: continue
#     n //= 2
#     left = i // 10 ** n
#     right = i % 10 ** n
#     t1 = sum(int(j) for j in str(left))
#     t2 = sum(int(k) for k in str(right))
#     if t1 == t2:
#         count += 1
# print(count)
# 大概1分钟，填空其实无所谓了

# 下面是大佬的想法
# 只需要遍历1到9999即可，建立两个二维数组，data1是可以作为头部的，data2是可以作为尾部的，
# 二维数组里面有四个一维数组，指在头尾部长度，一维数组的下标则表示数字之和，如在data1[2][9]中意思
# 就是头部长度为3，头部数字之和为9的组合数，其余的一个道理，注意的是，尾部赋值时是根据头部长度来赋值的，比如
# 头部是100，和是1，那尾部可以是001，010，100三种，但是不能是1000这样的，所以给个fork来赋值尾部，
# 最后同时遍历两个二维数组，c加上对应的头尾部相乘即可（为啥数组长度是4和37，因为头尾最长是99999999，10
# 0000000人为判断不行）

c = 0
data1 = [[0 for _ in range(37)] for __ in range(4)]
data2 = [[0 for _ in range(37)] for __ in range(4)]
for i in range(1, 10000):
    t = sum([int(j) for j in str(i)])
    l = len(str(i))
    data1[l - 1][t] += 1
    for k in range(l):
        data2[k][t] += 1
for a in range(4):
    for b in range(37):
        c += data1[a][b] * data2[a][b]
print(c)
