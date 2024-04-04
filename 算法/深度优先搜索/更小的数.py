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
s = input()
ans = 0
for i in range(len(s)):
    for j in range(i):
        a = i;b = j  # 这里的循环条件可能导致 i 和 j 的值在内部循环中被修改，影响外部循环的迭代次数
        while a > b:
            if s[a] <  s[b]:
                ans += 1
                break
            elif s[a] > s[b]:
                break
            elif s[a] == s[b]:
                a -= 1
                b += 1

print(ans)