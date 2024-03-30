class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        lst=sorted(nums)
        n=len(lst)
        lst2=[0]*n
        for i in range(1,n):
            if lst[i]-lst[i-1]==1:
                lst2[i]=1+lst2[i-1]
            elif lst[i]==lst[i-1]:
                lst2[i]=lst2[i-1]
            else:
                lst2[i]=0
        return max(lst2)+1