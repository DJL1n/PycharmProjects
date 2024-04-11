"""
作者：legionb
日期：2024年04月03日
"""
# n=input()
# res=0
#
# for i in range(len(n)):
#     for j in range(i):
#         while i>j:
#             if n[i]<n[j]:
#                 res+=1
#                 break
#             elif n[i]>n[j]:
#                 break
#             else:
#                 i-=1
#                 j+=1
# print(res)



# s = input()
# ans = 0
# for i in range(len(s)):
#     for j in range(i):
#         a = i;b = j  # 这里的循环条件可能导致 i 和 j 的值在内部循环中被修改，影响外部循环的迭代次数
#         while a > b:
#             if s[a] <  s[b]:
#                 ans += 1
#                 break
#             elif s[a] > s[b]:
#                 break
#             elif s[a] == s[b]:
#                 a -= 1
#                 b += 1
#
# print(ans)

s=[int(i) for i in input()]
# print(s)
n=len(s)
res=0
dp=[[0]*n for _ in range(n+1)]
for i in range(n-1):
    if s[i]>s[i+1]:
        dp[2][i]=1
        res+=1
for i in range(n-2):
    if s[i]>s[i+2]:
        dp[3][i]=1
        res+=1
for i in range(4,n+1):
    for j in range(n-i+1):
        if s[j]>s[j+i-1] or s[j]==s[j+i-1] and dp[i-2][j+1]==1:
            dp[i][j]=1
            res+=1
print(res)

