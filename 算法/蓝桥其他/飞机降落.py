"""
作者：legionb
日期：2024年04月11日
"""
def merge_sort(matrix):
    if len(matrix)>1:
        mid=len(matrix)//2
        left=matrix[:mid]
        right=matrix[mid:]

        merge_sort(left)
        merge_sort(right)

        i,j,k=0,0,0
        while i<len(left) and j <len(right):
            if left[i][0]+left[i][2]<right[j][0]+right[j][2]:
                matrix[k]=left[i]
                i+=1
            elif left[i][0]+left[i][2]>right[j][0]+right[j][2]:
                matrix[k]=right[j]
                j+=1
            else:
                if left[i][0]<right[j][0]:
                    matrix[k]=left[i]
                    i+=1
                else:
                    matrix[k]=right[j]
                    j+=1
            k+=1
        while i<len(left):
            matrix[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            matrix[k]=right[j]
            j+=1
            k+=1

def judge(time):
    print(time)
    # print([1]*N)
    if record==[1]*N:
        global whether
        whether+=True
        print(whether)
    for i in range(N):
        print(record)
        if record[i]==0:
            if time<=matrix[i][0]+matrix[i][1]:
                record[i]=1
                judge(max(time,matrix[i][0])+matrix[i][2])
                record[i]=0
            else:
                continue
    # print(matrix)
    # time=0
    # for i in range(N-1):
    #     time=max(time,matrix[i][0])
    #     time+=matrix[i][2]
    #     if time > matrix[i+1][0]+matrix[i+1][1]:
    #         print("NO")
    #         return
    # print("YES")
    # return

q=int(input())
for i in range(q):
    N=int(input())
    matrix=[list(map(int,input().split())) for _ in range(N)]
    record=[0]*N
    merge_sort(matrix)
    whether=False
    judge(0)
    # print(whether)