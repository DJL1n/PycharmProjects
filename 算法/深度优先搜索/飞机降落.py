"""
作者：legionb
日期：2024年04月11日
"""
def judge(time):
    # print(time)
    # print([1]*N)
    # print(record)
    if record==[1]*N:
        global whether
        whether=whether or True
        # print(whether)
    for i in range(N):
        # print(record)
        if record[i]==0 and time<=matrix[i][0]+matrix[i][1]:
            record[i]=1
            judge(max(time,matrix[i][0])+matrix[i][2])
            record[i]=0


q=int(input())
for i in range(q):
    N=int(input())
    matrix=[list(map(int,input().split())) for _ in range(N)]
    record=[0]*N

    whether=False
    judge(0)
    print("YES" if whether is True else "NO")