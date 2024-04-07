"""
作者：legionb
日期：2024年04月07日
"""
#python在不能一开始声明空列表，导致无法向C++那样对第一行和第一列直接进行求和公式
#需要在求和的过程中加入一些条件判断
# n,m=map(int,input().split())
# lst=[[0]*(m+1)]
# for i in range(n):
#     lst.append([0]+[int(j) for j in input().split()])
#最后还是选择了加入0，因为在求和还有求区间和的公式里面，没有0的参与要分好多情况
n,m=3,4
lst=[[0,0,0,0,0],[0,1,7,2,4],[0,3,6,2,8],[0,2,1,2,3]]
for i in range(1,n+1):
    for j in range(1,m+1):
        lst[i][j]+=lst[i-1][j]+lst[i][j-1]-lst[i-1][j-1]
print(lst)
x1,y1,x2,y2=1,3,3,4

# x1-=1
# x2-=1
# y1-=1
# y2-=1

print(lst[x2][y2]-lst[x1-1][y2]-lst[x2][y1-1]+lst[x1-1][y1-1])
