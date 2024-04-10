# """
# 作者：legionb
# 日期：2024年04月08日
# """
# import collections
#
# n, x = map(int, input().split())
# s = input()
# # print(s)
# deliver = [''] * x
# sweet = collections.defaultdict(int)
# # print(sweet)
# for i in s:
#     sweet[i] += 1
# lst = sorted(sweet.keys())
# print(lst)
# for i in lst:
#     while sweet[i] > 0:
#         index = deliver.index(max(deliver))
#         deliver[index] += i
#         sweet[i] -= 1
# print(sweet)
# print(max(deliver))

n,x=map(int,input().split())
sweets=list(input())
sweets.sort()
print(''.join(sweets[x-1:]))