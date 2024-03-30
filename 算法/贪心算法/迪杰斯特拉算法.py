"""
作者：legionb
日期：2024年03月23日
"""
from collections import defaultdict


def dijkstra(graph, start):
    # 初始化距离字典和已访问集合
    distances = {node: float('inf') for node in graph}
    visited = set()
    # 设置起始节点距离为0
    distances[start] = 0

    while len(visited) < len(graph):
        # 找到当前距离最短的未访问节点
        current_node = min((node for node in graph if node not in visited), key=lambda x: distances[x])
        visited.add(current_node)

        # 更新当前节点的邻居节点距离
        for neighbor, weight in graph[current_node].items():
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight

    return distances


# 测试
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
start_node = 'A'
result = dijkstra(graph, start_node)
print("Shortest distances from node", start_node, ":")
for node, distance in result.items():
    print("To node", node, ":", distance)
