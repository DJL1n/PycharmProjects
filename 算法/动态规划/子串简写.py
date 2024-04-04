"""
作者：legionb
日期：2024年04月03日
"""
k=int(input())
str1,start,end=input().split()
n=len(str1)
dp=[0]*(n+1)
res=0
for i in range(n):
    if str1[i]==start:
        dp[i+1]=dp[i]+1
    else:
        dp[i+1]=dp[i]
        if str1[i]==end:
            res+=dp[i-k+2]
print(res)