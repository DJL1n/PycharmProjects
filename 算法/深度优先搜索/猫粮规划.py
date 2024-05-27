"""
作者：legionb
日期：2024年05月27日
"""
def DFS(index,energy):
    global res

    energy+=W[index]
    if energy>r:
        return
    if energy<l and (index==n-1 or energy+backSum[index+1]<l):
        return
    if l<=energy<=r:
        res+=1
    for i in range(index+1,n):
        DFS(i,energy)


n,l,r=map(int,input().split())
W=list(map(int,input().split()))
record=[0]*n
backSum=W[:]
for i in range(n):
    if W[i]>r:
        record[i]=1
for i in range(n-2,-1,-1):
    backSum[i]+=backSum[i+1]
res=0
for i in range(n):
    DFS(i,0)
# print(backSum)
print(res)