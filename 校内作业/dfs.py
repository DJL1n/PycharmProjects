"""
作者：legionb
日期：2024年06月09日
"""
from collections import deque


def dfs(adj_matrix):
    color = []
    tree_arcs = []
    forward_arcs = []
    back_arcs = []
    cross_arcs = []
    seen = []
    done = []
    for i in range(len(adj_matrix)):
        color.append(0)
        seen.append(0)
        done.append(0)
    time = 0
    for i in range(len(adj_matrix)):
        if color[i] == 0:
            tree, forward, back, cross, time = dfs_visit(adj_matrix, i, color, seen, done, time)
            tree_arcs += tree
            forward_arcs += forward
            back_arcs += back
            cross_arcs += cross

    tree_arcs = list(tree_arcs)
    tree_arcs.sort(key=lambda x: str(x[0]) + str(x[1]))
    forward_arcs = list(forward_arcs)
    forward_arcs.sort(key=lambda x: str(x[0]) + str(x[1]))
    back_arcs = list(back_arcs)
    back_arcs.sort(key=lambda x: str(x[0]) + str(x[1]))
    cross_arcs = list(cross_arcs)
    cross_arcs.sort(key=lambda x: str(x[0]) + str(x[1]))
    return tree_arcs, forward_arcs, back_arcs, cross_arcs


def dfs_visit(adj_matrix, s, color, seen, done, time):
    tree = set()
    forward = set()
    back = set()
    cross = set()
    cur_time = time
    stack = deque()

    stack.append(s)
    color[s] = 1
    seen[s] = cur_time
    cur_time += 1

    while len(stack) > 0:
        r = stack[-1]  # pick the top
        done_flag = True
        for j in range(len(adj_matrix[r])):
            if adj_matrix[r][j] > 0:
                if color[j] == 0:
                    color[j] = 1
                    stack.append(j)
                    tree.add((r, j))
                    seen[j] = cur_time
                    cur_time += 1
                    done_flag = False
                    break
                elif color[j] == 1:
                    back.add((r, j))
                else:
                    if seen[r] < seen[j] and (r, j) not in tree:
                        forward.add((r, j))
                    elif seen[j] < seen[r] and (r, j) not in tree:
                        cross.add((r, j))
                        print(seen[r],r)
                        print(seen[j],j)

        if done_flag:
            stack.pop()
            done[r] = cur_time
            cur_time += 1
            color[r] = 2
    return tree, forward, back, cross, cur_time
