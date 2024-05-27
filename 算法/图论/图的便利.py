"""
作者：legionb
日期：2024年05月27日
"""
def find_max(i,j):
    j=max(max(dict[i]),j)
    for node in dict[i]:


N,M=map(int,input().split())
graph={}
for i in range(M):
    u,v=map(int,input().split())
    if u not in graph:
        graph[u]=[]
    graph[u].append(v)

res=[]
for i in range(1,N+1):
    record=set()
