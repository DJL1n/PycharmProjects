"""
作者：legionb
日期：2024年02月25日
"""
def bag0_1(w:int,V:list, W:list)->int:
    n=len(V)
    dp=[[0]*(w+1) for _ in range(n+1)]
    for i in range(0,n):
        for j in range(0,w):
            if W[i]>j: dp[i+1][j]=dp[i][j]
            else: dp[i+1][j]=max(dp[i][j],dp[i][j-W[i]]+V[i])
    return dp[n][w]
