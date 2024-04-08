"""
作者：legionb
日期：2024年04月08日
"""
n = int(input())
num = list(map(int, input().split()))
nums = []
for i in range(n - 1):
    nums.append(list(map(int, input().split())))
nums.append([0, 0])
min_door = [num[0] + nums[0][0] / 0.7] + [0.0] * (n - 1)
min_bottom = [num[0]] + [0.0] * (n - 1)
for i in range(1, n):
    interval = num[i] - num[i - 1]
    if nums[i - 1][1] >= nums[i][0]:
        min_door[i] = min(min_door[i - 1] + (nums[i - 1][1] - nums[i][0]) / 1.3,
                          min_bottom[i - 1] + interval + nums[i][0] / 0.7)
    else:
        min_door[i] = min(min_door[i - 1] + (nums[i][0] - nums[i - 1][1]) / 0.7,
                          min_bottom[i - 1] + interval + nums[i][0] / 0.7)
    min_bottom[i] = min(min_bottom[i - 1] + interval, min_door[i - 1] + nums[i - 1][1] / 1.3)
print(min_door)
print(min_bottom)
print("%.2f" % min_bottom[-1])