"""
作者：legionb
日期：2024年06月13日
"""
def is_reachable(adj_matrix,s,d):
    n=len(adj_matrix)
    reachable=[0]*n
    result=[False]
    dfs(s,d,adj_matrix,reachable,result)
    return result[0]

def dfs(s,d,graph,record,result):
    # print(record)
    if s==d:
        result[0]=True
    n=len(graph)
    for i in range(n):
        if graph[s][i]==1 and record[i]==0:
            record[i]=1
            dfs(i,d,graph,record,result)
            record[i]=0

adj_matrix = [[0,1,1,0],[0,0,1,0],[1,0,0,0],[0,1,0,0]]
print(is_reachable(adj_matrix, 0, 3))
print(is_reachable(adj_matrix, 3, 0))