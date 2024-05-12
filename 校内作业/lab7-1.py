"""
作者：legionb
日期：2024年05月12日
"""
from collections import deque


def find_girth(adj_list):
    n = len(adj_list)  # Number of vertices
    if n == 0:
        return 'inf'

    # Initialize distances from each vertex to all others as infinity
    distance = [[float('inf')] * n for _ in range(n)]

    # Set the distance from each vertex to itself to 0
    for i in range(n):
        distance[i][i] = 0

    # Perform BFS for each vertex to find the shortest cycle
    for start in range(n):
        queue = deque([(start, start, 0)])  # (current vertex, parent vertex, distance)
        while queue:
            current, parent, dist = queue.popleft()
            for neighbor in adj_list[current]:
                if neighbor != parent:  # Avoid backtracking to the parent
                    if distance[current][neighbor] == float('inf'):
                        # If we find a shorter path, update the distance and add the edge to the queue
                        distance[current][neighbor] = dist + 1
                        queue.append((neighbor, current, dist + 1))
                    elif distance[current][neighbor] == dist + 1:
                        # If we find an alternative path of the same length, it's a cycle
                        return dist + 2  # The girth is the length of the cycle

    # If no cycle is found, return 'inf'
    return 'inf'

adj_list = [[2],[3],[0,3],[1,2,4,5],[3],[3]]
print(find_girth(adj_list))