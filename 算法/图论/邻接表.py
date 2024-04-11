"""
作者：legionb
日期：2024年04月11日
"""
from collections import defaultdict

# 对于松散图效率更高，但是要求图不带权重
class GraphAdjacencyList:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, start, end):
        self.graph[start].append(end)  # 有向图只需要写这一个
        self.graph[end].append(start)


# 例子
graph_list = GraphAdjacencyList()
graph_list.add_edge(0, 1)
graph_list.add_edge(1, 2)
graph_list.add_edge(2, 3)
graph_list.add_edge(3, 4)
print(graph_list.graph)
