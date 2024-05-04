"""
作者：legionb
日期：2024年05月04日
"""


def pivot(mylist, l, r):
    return r

def partition(mylist, l, r, pivot_index):
    pivot_value=mylist[pivot_index]
    store_index=l

    for i in range(l,r+1):
        if mylist[i]<=pivot_value:
            mylist[i],mylist[store_index]=mylist[store_index],mylist[i]
            store_index+=1

    return store_index-1

def quicksort(mylist, l, r):
    if l < r:
        pi = pivot(mylist, l, r)
        k = partition(mylist, l, r, pi)
        print("pivot=" + str(mylist[k]) + " " + "L=" + str(l) + " " + "R=" + str(r))
        print(mylist)
        quicksort(mylist, l, k - 1)
        quicksort(mylist, k + 1, r)

mylist = [23, 12, 31, 21, 41, 3, 1]
print(mylist)
quicksort(mylist, 0, len(mylist) - 1)
print(mylist)