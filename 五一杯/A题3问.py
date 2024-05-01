import numpy as np
import random

# 假设我们有一组矩形块，每个矩形块由其索引和四个坐标(x1, y1, x2, y2)定义
rectangles = [
    (0, 0, 4, 3),
    (6, 0, 10, 3),
    (12,0,16,3),
    (18,0,22,3),
    (0,5,4,8),
    (6,5,10,8),
    (12,5,16,8),
    (18,5,22,8),
    (0,10,4,13),
    (6,10,10,13),
    (12,10,16,13),
    (18,10,22,13)
    # ... 添加所有矩形块的坐标
]

# 计算矩形块之间的距离矩阵
def calculate_distance_matrix(rectangles):
    n = len(rectangles)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            # 计算两个矩形块中心点之间的距离
            dx = (rectangles[j][2] + rectangles[j][0]) / 2 - (rectangles[i][2] + rectangles[i][0]) / 2
            dy = (rectangles[j][3] + rectangles[j][1]) / 2 - (rectangles[i][3] + rectangles[i][1]) / 2
            distance_matrix[i, j] = np.sqrt(dx ** 2 + dy ** 2)
            distance_matrix[j, i] = distance_matrix[i, j]  # 距离矩阵是对称的
    return distance_matrix


# 遗传算法参数
population_size = 50
generations = 100
mutation_rate = 0.01

# 随机生成初始种群
population = [random.sample(range(len(rectangles)), len(rectangles)) for _ in range(population_size)]


# 计算适应度
def calculate_fitness(individual, distance_matrix):
    # 闭合路径，最后一个矩形块回到第一个矩形块的距离
    return 1 / (sum(
        distance_matrix[individual[i], individual[(i + 1) % len(rectangles)]] for i in range(len(rectangles))) +
                distance_matrix[individual[-1], individual[0]])


# 选择过程
def selection(population, fitness, num_parents):
    parents = random.choices(population, weights=fitness, k=num_parents)
    return parents


# 交叉过程
def crossover(parent1, parent2):
    child1 = parent1.copy()
    child2 = parent2.copy()
    # 单点交叉
    crossover_point = random.randint(1, len(rectangles) - 1)
    child1[crossover_point:], child2[crossover_point:] = parent2[crossover_point:], parent1[crossover_point:]
    return child1, child2


# 变异过程
def mutation(individual, mutation_rate, distance_matrix):
    if random.random() < mutation_rate:
        idx1, idx2 = random.sample(range(len(rectangles)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    # 确保路径闭合
    last_idx = individual.index(random.choice(individual))
    individual.insert(0, individual[last_idx])
    individual.pop(last_idx + 1)
    return individual


# 遗传算法主循环
for generation in range(generations):
    distance_matrix = calculate_distance_matrix(rectangles)
    fitness = np.array([calculate_fitness(ind, distance_matrix) for ind in population])
    # 选择
    selected = selection(population, fitness, population_size // 2)
    # 交叉和变异
    offspring = [crossover(parent1, parent2) for parent1, parent2 in zip(selected[::2], selected[1::2])]
    offspring = [mutation(child, mutation_rate, distance_matrix) for child in offspring]
    population = [child for pair in offspring for child in pair]

# 最佳解
best_fitness_idx = np.argmax(fitness)
best_path = population[best_fitness_idx]
print("Best path:", [rectangles[i] for i in best_path])
print("Best fitness (path length):", fitness[best_fitness_idx])
