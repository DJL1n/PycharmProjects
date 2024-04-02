"""
作者：legionb
日期：2024年04月02日
"""
N,K=map(int,input().split())
A=[int(input()) for _ in range(N)]
count=0
for i in range(N):
    for j in range(i+1,N+1):
        if sum(A[i:j])%K==0:
            count+=1
            # print(A[i:j])
print(count)