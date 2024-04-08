# """
# 作者：legionb
# 日期：2024年04月07日
# """
# n=int(input())
# lst=[list(map(int,input().split())) for _ in range(3)]
# b=[0,0,0]
# res=-1
# count=0
# record=[True]*n
# A=[0]*n
# for i in range(n):
#     A[i]=abs(lst[0][i]-lst[1][i])+abs(lst[1][i]-lst[2][i])+abs(lst[2][i]-lst[0][i])
# numbered_list=[(id,value) for id,value in enumerate(A)]
# numbered_list.sort(key=lambda x:x[1],reverse=True)
# while count<n:
#     if b[0]>b[1]+b[2] or b[1]>b[0]+b[2] or b[2]>b[0]+b[1]:
#         res=max(count,res)
#     for i in range(3):
#         b[i]+=lst[i][numbered_list[count][0]]
#     count+=1
# print(res)

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
# print(A)
X = sorted([A[i] - B[i] - C[i] for i in range(n)],reverse=True)
Y = sorted([B[i] - C[i] - A[i] for i in range(n)],reverse=True)
Z = sorted([C[i] - A[i] - B[i] for i in range(n)],reverse=True)
# print(X)
res_X, res_Y, res_Z, res = 0, 0, 0, 0

for i in range(n):
    res_X += X[i]
    res_Y += Y[i]
    res_Z += Z[i]
    if res_X > 0: res = max(res, i + 1)
    if res_Y > 0: res = max(res, i + 1)
    if res_Z > 0: res = max(res, i + 1)

print(res if res > 0 else -1)
