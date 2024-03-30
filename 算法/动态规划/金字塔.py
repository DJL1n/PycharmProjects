nums=[[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
n=5
dp=nums[n-1]
for i in range(n-2,-1,-1):
    for j in range(i+1):
        dp[j]=max(dp[j],dp[j+1])+nums[i][j]
        print(dp)
    print()

print(dp)