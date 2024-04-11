"""
作者：legionb
日期：2024年04月11日
"""


class GraphAdjacencyMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, start, end):
        self.matrix[start][end] = 1  # 有向图一个就够了
        self.matrix[end][start] = 1
