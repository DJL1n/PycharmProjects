def DFS(cur):
    if cur==n:
        res.append(max(lst))
        # print(lst)
        return
    for i in range(x):
        lst[i]+=sweets[cur]
        DFS(cur+1)
        lst[i]=lst[i][:-1]


n,x=map(int,input().split())
sweets=list(input())
sweets.sort()
lst=sweets[:x]
res=[]
DFS(x)
# print(res)
print(min(res))