# def DFS(cur):
#     if cur == n:
#         res.append(max(lst))
#         # print(lst)
#         return
#     for i in range(x):
#         lst[i] += sweets[cur]
#         DFS(cur + 1)
#         lst[i] = lst[i][:-1]


n, x = map(int, input().split())
sweets = list(input())
sweets.sort()
# lst = sweets[:x]
# res = []
# DFS(x)
# # print(len(res))
# print(min(res))
if sweets[0]!=sweets[x-1]:
    print(sweets[x-1])
else:
    if sweets[x]==sweets[-1]:
        for i in range(0,n,x):
            print(sweets[i],end="")
    else:
        print(sweets[0]+''.join(sweets[x:]))