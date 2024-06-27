def find_girth(adj_list):
    n = len(adj_list)
    result = float("inf")
    visited = [float("inf")] * n  # 初始化visited数组

    def DFS(cur, parent, dist):
        nonlocal result
        visited[cur] = dist
        for node in adj_list[cur]:
            if visited[node]==float("inf"):  # 如果节点未访问，继续DFS
                DFS(node, cur, dist + 1)
            elif node != parent:  # 发现环
                cycle_length = dist - visited[node] + 1
                if cycle_length >=3:
                    result = min(result, cycle_length)

    for i in range(n):  # 从每个顶点开始DFS
        visited = [float("inf")] * n  # 重置visited数组
        DFS(i, -1, 1)  # 从顶点i开始，-1表示没有父节点

    return result

adj_list = [[1,5],[0,2],[1,3],[2,4],[3,5],[0,4]]
print(find_girth(adj_list))