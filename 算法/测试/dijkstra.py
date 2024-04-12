"""
作者：legionb
日期：2024年04月12日
"""
import heapq
def dijkstra(graph,start):
    distances={vertex:float('inf') for vertex in graph}
    distances[start]=0
    priority_queue=[(0,start)]
    while priority_queue:
        current_dis,current_vertex=heapq.heappop(priority_queue)
        if current_dis>distances[current_vertex]:
            continue
        for neighbor,weight in graph[current_vertex].items():
            distance=distances[current_vertex]+weight
            if distance<distances[neighbor]:
                distances[neighbor]=distance
                heapq.heappush(priority_queue,(distance,neighbor))
    return distances



# 示例
graph_weighted = {
    0: {1: 1, 2: 4},
    1: {0: 1, 2: 2, 3: 5},
    2: {0: 4, 1: 2, 3: 1},
    3: {1: 5, 2: 1}
}
print(graph_weighted[0].items())
shortest_distances = dijkstra(graph_weighted, 0)
print("Shortest Distances:", shortest_distances)