"""
作者：legionb
日期：2024年06月27日
"""
def find_scc(adj_lists):
    def convert():
        lst=[[0]*n for i in range(n)]
        for i in range(n):
            for j in adj_lists[i]:
                lst[i][j]=1
        return lst
    def transform():
        lst=[[0]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                lst[i][j]=adj_matrix[j][i]
        return lst
    def DFS(lst,start):
        visited[start]=1
        record.append(start)
        for next in range(n):
            if lst[start][next]==1 and visited[next]==0:
                DFS(lst,next)
        return
    n=len(adj_lists)
    adj_matrix=convert()
    trans_matrix=transform()
    visited=[0]*n
    record=[]
    DFS(trans_matrix,0)

