"""
作者：legionb
日期：2024年06月27日
"""
import heapq


def schedule(dep):
    n=len(dep)
    in_degree={}
    q = []
    for i in range(n):
        if len(dep[i])==0:
            q.append(i)
        else:
            in_degree[i]=len(dep[i])
    result=[]
    while q:
        cur=heapq.heappop(q)
        result.append(cur)
        for i in range(n):
            if cur in dep[i]:
                in_degree[i]-=1
                if in_degree[i]==0:
                    heapq.heappush(q,i)
                    # print(i)
        # print(in_degree)
    return result if len(result)==n else None
dep = [[1,2],[3,5],[3],[6,7,8],[5],[6,9],[8],[8],[9],[]]
print(schedule(dep))



