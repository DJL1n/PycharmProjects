"""
作者：legionb
日期：2024年04月14日
"""


def pivot(mylist, l, r):
    if r-l==1:
        return l
    lst=[]
    lst.append((l,mylist[l]))
    lst.append((r,mylist[r]))
    lst.append(((r-l)//2,mylist[(r-l)//2]))
    return sorted(lst,key=lambda x:x[1])[1][0]


def partition(mylist, l, r, pivot_index):
    pivot=mylist[pivot_index]
    start,end=l,r
    while start<end:
        while start<end and mylist[start]<pivot:
            start+=1
        mylist[end]=mylist[start]
        while start<end and mylist[end]>pivot:
            end-=1
        mylist[start]=mylist[end]
    mylist[end]=pivot
    return end

def quicksort(mylist, l, r):
    if l < r:
        pi = pivot(mylist, l, r)
        k = partition(mylist, l, r, pi)
        print("pivot=" + str(mylist[k]) + " " + "L=" + str(l) + " " + "R=" + str(r))
        print(mylist)
        quicksort(mylist, l, k - 1)
        quicksort(mylist, k + 1, r)


mylist = [23, 12, 31, 21]
print(mylist)
quicksort(mylist, 0, len(mylist) - 1)
print(mylist)