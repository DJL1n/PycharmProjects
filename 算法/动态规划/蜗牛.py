"""
作者：legionb
日期：2024年04月08日
"""
# 泪目了，改了一天了，记录一下错误的地方
# 如果只是2行的动态规划下次还是用两个1维列表吧，折磨死了，上下行经常搞混
# 要好好审题啊，那个传递列表的内容完全搞错了，导致动态规划想的太复杂了，而且还是得自己手写啊，真想真没用啊
n = int(input())
lst = [0] + [int(_) for _ in input().split()]
transmit = [[]]

for i in range(n - 1):
    transmit.append(list(map(int, input().split())))
transmit.append([0, 0])
print(transmit)
dp = [[0.0] * (n + 1) for _ in range(2)]  # 第一行是传送点的最短，第二行是树的底最短
# 开头
dp[0][1] = lst[1] + transmit[1][0] / 0.7
dp[1][1] = lst[1]
# preStatus=False
for i in range(2, n + 1):
    interval = lst[i] - lst[i - 1]  # 计算相邻数的水平距离
    if transmit[i - 1][1] >= transmit[i][0]:  # 出口在上面，往下移
        # 先考虑到下一个传送点，包含两步，先出来，再上下移动到下一个传送点口
        dp[0][i] = min(dp[0][i - 1] + (transmit[i - 1][1] - transmit[i][0]) / 1.3,
                       dp[1][i - 1] + interval + transmit[i][0] / 0.7)
    else:  # 出口在下，往上移动
        dp[0][i] = min(dp[0][i - 1] + (transmit[i][0] - transmit[i - 1][1]) / 0.7,
                       dp[1][i - 1] + interval + transmit[i][0] / 0.7)
    # 再考虑树底
    dp[1][i] = min(dp[0][i - 1] + transmit[i - 1][1] / 1.3,
                   dp[1][i - 1] + interval)

# res= min(dp[0][n-1] + transmit[n - 1][1] / 1.3, dp[1][n - 1]) + lst[n] - lst[n - 1]


print(dp)
print("%.2f" % dp[1][-1])
