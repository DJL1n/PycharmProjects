"""
作者：legionb
日期：2024年04月05日
"""
nums=list(map(int,input().split()))
n=len(nums)
res=[]
nums.sort()
pre=float("inf")
for i in range(n):
    left=i+1
    right=n-1
    while left<right:
        total=nums[i]+nums[left]+nums[right]
        if total==0:
            if pre==nums[left]:
                continue
            res.append([nums[i],nums[left],nums[right]])
            pre=nums[left]
            break
        elif total>0:
            right-=1
        else:
            left+=1
        # return res
print(res)