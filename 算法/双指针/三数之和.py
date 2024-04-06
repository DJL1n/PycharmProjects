"""
作者：legionb
日期：2024年04月05日
"""
# 对撞指针
# 基本思路，调用双指针减少循环数
nums = list(map(int, input().split()))
n = len(nums)
res = []
nums.sort()
pre = float("inf")  # 第一次去重，存储上一个的第一个数，去除第一个数相同的情况
for i in range(n):
    if pre == nums[i]:
        continue
    left = i + 1
    right = n - 1
    while left < right:
        total = nums[i] + nums[left] + nums[right]
        if total == 0:
            res.append([nums[i], nums[left], nums[right]])
            temp = nums[left]  # 第二次去重，去除第一个和第二个数都相同的情况
            while left < right and temp == nums[left]:  # 并且继续查找是否有其他的可能
                left += 1
        elif total > 0:
            right -= 1
        else:
            left += 1
        # return res
    pre = nums[i]
print(res)
