"""
作者：legion
日期：2024年04月12日
"""
import heapq


# 这个代码里面的字典和列表是混用的，实际上字典覆盖面更全，但是这题是数字作为索引，那么列表也行
# 实在是太难想了，明知道迪杰斯特拉算法，但是没有理解到
# 迪杰斯特拉算法确实是求最短路径的算法，但是我之前的思路是求完所有情况了再尝试去掉连续个加权数，但是实际上，迪杰斯特拉算法是基于目前情况的最优算法，也就是说，前面的删去的权重要和下一种情况一起考虑
def dijkstra():
    distances = [[10 ** 6] * N for i in range(N)]
    distances[0][0] = 0
    priority_queue = [(0, 0)]
    while priority_queue:
        cur_v, cur_dist = heapq.heappop(priority_queue)
        # print(cur_v)
        # print(graph)
        for neighbor, weight in graph[cur_v].items():
            flag = False  # 这个变量是来检测是否找到更优情况的，当改变发生时，就要上传优先队列
            # 下面是正常的思路，目前点加上临界点是否比记录的到这个点的最小距离更小，经典dp思想
            if distances[cur_v][0] + weight < distances[neighbor][0]:
                distances[neighbor][0] = distances[cur_v][0] + weight
                flag = True
            if distances[cur_v][K] + weight < distances[neighbor][K]:
                flag = True
                distances[neighbor][K] = distances[cur_v][K] + weight
            # 这里是解法的精髓所在
            # 如果前面连续K个加权删去了比原来小，那就继承
            # 这里也不算太懂，因为正常来说，只要是少了一段，都应该小啊
            for j in range(1, K + 1):
                if distances[neighbor][j] > distances[cur_v][j - 1]:
                    flag = True
                    distances[neighbor][j] = distances[cur_v][j - 1]
            if flag is True:
                heapq.heappush(priority_queue, (neighbor, distances[neighbor][0]))
    # print(distances)
    print(min(distances[N - 1][0], distances[N - 1][K]))


N, K, M = map(int, input().split())
graph = {}
for i in range(M):
    u, v, w = map(int, input().split())
    # 这俩要小心，是后加而不是覆盖
    if u not in graph:
        graph[u] = {}
    if v not in graph:
        graph[v] = {}
    graph[u][v] = w
    graph[v][u] = w
# print(graph)
dijkstra()
