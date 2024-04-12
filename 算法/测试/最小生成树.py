"""
作者：legionb
日期：2024年04月12日
"""
import heapq


def prim(graph):
    start = list(graph.keys())[0]
    visited = {start}
    priority_queue = [
        (weight, start, end)
        for end, weight in graph[start].items()
    ]
    heapq.heapify(priority_queue)
    mini_spinning_tree = []

    while priority_queue:
        weight, from_vertex, to_vertex = heapq.heappop(priority_queue)
        if to_vertex not in visited:
            visited.add(to_vertex)
            mini_spinning_tree.append((from_vertex, to_vertex, weight))
            for neighbor, neighbor_weight in graph[to_vertex].items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (neighbor_weight, to_vertex, neighbor))
    return mini_spinning_tree


# 示例
graph_weighted = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
minimum_spanning_tree = prim(graph_weighted)
print("Minimum Spanning Tree:", minimum_spanning_tree)
