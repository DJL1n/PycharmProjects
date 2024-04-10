# """
# 作者：legionb
# 日期：2024年04月10日
# """
# import collections
# from collections import deque
# class MaxQueue:
#     def __init__(self):
#         self.queue=deque()
#     def push(self,value):
#         while self.queue and self.queue[-1]<value:
#             self.queue.pop()
#         self.queue.append(value)
#     def max(self):
#         return self.queue[0]
# class MinQueue:
#     def __init__(self):
#         self.queue=deque()
#     def push(self,value):
#         while self.queue and self.queue[-1]>value:
#             self.queue.pop()
#         self.queue.append(value)
#     def min(self):
#         return self.queue[0]
#
# n,m,a,b=map(int,input().split())
# matrix=[list(map(int,input().split())) for _ in range(n)]
#
# result=0
# min_dp=[[0]*m for _ in range(n)]
# max_dp=[[0]*m for _ in range(n)]
# for i in range(n):
#     for j in range(m-b+1):
#         m1=MinQueue()
#         m2=MaxQueue()
#         for k in range(b):
#             m1.push(matrix[i][j+k])
#             m2.push(matrix[i][j+k])
#         min_dp[i][j]=m1.min()
#         max_dp[i][j]=m2.max()
# # print(min_dp)
# # print(max_dp)
# for j in range(m-b+1):
#     for i in range(n-a+1):
#         l1=MinQueue()
#         l2=MaxQueue()
#         for k in range(a):
#             l1.push(min_dp[i+k][j])
#             l2.push(max_dp[i+k][j])
#         result+=l1.min()*l2.max()
# print(result)

# 理论上这个方法是正确的，但是运行效率太低，超时了一半，所以直接考虑用冒泡试试

n, m, a, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
result = 0

# 横向找区间最小和最大
min_dp = [[0] * m for _ in range(n)]
max_dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m - b + 1):
        m1 = matrix[i][j]
        m2 = matrix[i][j]
        for k in range(1, b):
            m1 = matrix[i][j + k] if matrix[i][j + k] < m1 else m1
            m2 = matrix[i][j + k] if matrix[i][j + k] > m2 else m2
        min_dp[i][j] = m1
        max_dp[i][j] = m2
# print(min_dp)
# print(max_dp)

# 纵向找这个子矩阵的最大最小值
for j in range(m - b + 1):
    for i in range(n - a + 1):
        m1 = min_dp[i][j]
        m2 = max_dp[i][j]
        for k in range(1, a):
            m1 = min_dp[i + k][j] if min_dp[i + k][j] < m1 else m1
            m2 = max_dp[i + k][j] if max_dp[i + k][j] > m2 else m2
        result += m1 * m2
print(result)
