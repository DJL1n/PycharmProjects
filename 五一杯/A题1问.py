"""
作者：legionb
日期：2024年05月01日
"""
# 伪代码：使用 Dijkstra 算法找到最短路径
def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    visited = set()

    while not all(node in visited for node in graph):
        node = min((node for node in graph if node not in visited), key=lambda node: distances[node])
        visited.add(node)

        for neighbor, distance in graph[node].items():
            if distance + distances[node] < distances[neighbor]:
                distances[neighbor] = distance + distances[node]

    return distances

# 图表示为邻接表
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

shortest_paths = dijkstra(graph, 'A')
print(shortest_paths)