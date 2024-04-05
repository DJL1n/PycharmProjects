"""
作者：legionb
日期：2024年04月05日
"""
import queue


def swap(lst1, i, j):
    lst = lst1[:]
    lst[i], lst[j] = lst[j], lst[i]
    lst[-1] += 1
    return lst


start = list(input()); end = list(input())
n = len(start)
move = [3, -3, 2, -2, 1, -1]
record = queue.Queue()
record.put(start + [0])


repe={"".join(start)}
while not record.empty():
    item = record.get()
    index = item.index("*")
    if item[:n] == end:
        break
    for i in move:
        if -1<i+index<n:
            lst=swap(item,index,i+index)
            if "".join(lst[:n]) not in repe:
                repe.add("".join(lst[:n]))
                record.put(lst)

print(item[-1])

# 第一个方法是正常广搜，随机寻找和结果相同的列表，时间超时
# 转而想到第二种思路，可不可以不跳青蛙了，跳空杯子，改成跳杯子的深搜


# def dfs(i,k,item,level):#i是空杯的位置
#     global res
#     if level>=res:
#         return
#     if i==k:
#         if item==end:
#             res=min(res,level)
#             return
#     for j in move:
#         if -1<i+j<n:
#             lst=item[:]
#             lst[i],lst[i+j]=lst[i+j],lst[i]
#             # print(lst)
#             dfs(i+j,k,lst,level+1)
# res=20
# dfs(start.index("*"),end.index("*"),start,0)
# print(res)

# 第三种贪心,我就先让“*”到位，再去除其他不同的
