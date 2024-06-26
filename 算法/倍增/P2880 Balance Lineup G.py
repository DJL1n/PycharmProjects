"""
作者：legionb
日期：2024年04月08日
"""
#针对RMQ（区间最值问题）：给定长度为n的静态数列，做m次询问，每次给定L，R<=n，查询区间[L,R]内的最值
#适用于最小生成树
#最小生成树问题是指在一个链接了所有节点的图中，找到一个生成树，使得树中所有边的权值之和最小
# nlogn
#原理:一个区间若能被两个小区间覆盖，那么大区间的最值等于两个小区间的最值
#ps，感觉这个思想跟动态规划不谋而合，都是想象是某个状态然后继承上一个状态
#步骤：1.把数列分成很多小区间，并提前计算出每个小区间的最值；2.对任意一个区间最值查询，找到覆盖它的两个小区间，用两个小区间的最值算出答案
#而整体分块的思想就运用到了倍增

def ST_init():
    # dp[left][length]
    length = 1
    while length < n:
        length <<= 2
    dp = [[0] * length for i in range(n)]



n,q=map(int,input().split())
cows=[int(i) for i in range(n)]
ques=[list(map(int,input().split())) for i in range(q)]


