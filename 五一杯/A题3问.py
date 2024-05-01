import numpy as np
import random
import math

from scipy.spatial.distance import cdist

# 假设我们有一组点的坐标
points = np.array([
    [0, 0],
    [6, 0],
    [12, 0],
    [18, 0],
    [0, 5],
    [6, 5],
    [12, 5],
    [18, 5],
    [0, 10],
    [6, 10],
    [12, 10],
    [18, 10]
])

# 计算距离矩阵
dist_matrix = cdist(points, points)

# 模拟退火参数
initial_temp = 10000.0
alpha = 0.9
max_iterations = 5000
neighborhood_size = 3

# 模拟退火过程
current_temp = initial_temp
best_path = None
best_length = float('inf')

while current_temp > 0.01:
    new_path = list(range(len(points)))
    for _ in range(neighborhood_size):
        a, b = random.sample(new_path, 2)
        new_path[a], new_path[b] = new_path[b], new_path[a]

    new_length = sum(dist_matrix[(new_path[i], new_path[(i + 1) % len(points)])] for i in range(len(points)))

    if new_length < best_length or random.random() < math.exp((best_length - new_length) / current_temp):
        best_path = new_path
        best_length = new_length

    current_temp *= alpha

# 输出结果
print("Optimal cutting order:", [points[i] for i in best_path])
print("Total length of the cutting path:", best_length)