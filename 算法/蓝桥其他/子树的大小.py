# """
# 作者：legionb
# 日期：2024年04月08日
# """
# def ChildtreeSize(n,m,k):
#     if k>n:
#         return 0
#     # global count
#     count=1
#     for i in range(-1,m-1):
#         count+=ChildtreeSize(n,m,m*k-i)
#     return count
#
# N=int(input())
# # lst=[0]+[1]*10**9
# # n=len(lst)
# # for i in range(1,n):
# #     lst[i]+=lst[i-1]
# for i in range(N):
#     # count=0
#     n,m,k=map(int,input().split())
#     print(ChildtreeSize(n,m,k))
#

N=int(input())
for i in range(N):
    n,m,k=map(int,input().split())
    l=k
    level=0
    count=0
    while k<=n:
        l=l*m-(m-2)
        k=k*m+1
        count+=m**level
        level+=1
    print(count+n-l+1 if l<=n else count)

    m**level