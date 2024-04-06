# 滑动窗口
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
count = 0
res = 0
n = len(nums)
left, right = 0, 0
while right < n:
    if nums[right] == 1 or count < k:
        count += 1 if nums[right] == 0 else 0
        right += 1
        # print(count)
        continue
    res = max(res, right - left)
    # print(1)
    count += 1
    right += 1
    while count > k:  # 缩小窗口
        count -= 1 if nums[left] == 0 else 0
        left += 1
        # print(2)
res = max(res, right - left)
print(res)
