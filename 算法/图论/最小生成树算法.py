"""
作者：legionb
日期：2024年04月11日
"""
import heapq


def prim(graph):
    start_vertex = list(graph.keys())[0]
    visited = {start_vertex}
    edges = [
        (cost, start_vertex, to_vertex)
        for to_vertex, cost in graph[start_vertex].items()
    ]
    heapq.heapify(edges)
    minimum_spanning_tree = []
    while edges:
        cost, from_vertex, to_vertex = heapq.heappop(edges)
        if to_vertex not in visited:
            visited.add(to_vertex)
            minimum_spanning_tree.append((from_vertex, to_vertex, cost))
            for neighbor, neighbor_cost in graph[to_vertex].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (neighbor_cost, to_vertex, neighbor))
    return minimum_spanning_tree


# 示例
graph_weighted = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
minimum_spanning_tree = prim(graph_weighted)
print("Minimum Spanning Tree:", minimum_spanning_tree)
