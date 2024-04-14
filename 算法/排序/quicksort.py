"""
作者：legionb
日期：2024年04月14日
"""
def quicksort(lst,start,end):
    if start>=end:
        return
    standard,left,right=lst[start],start,end
    while left<right:
        while left<right and lst[right]>standard:
            right-=1
        lst[left]=lst[right]
        while left<right and lst[left]<standard:
            left-=1
        lst[right]=lst[left]
    lst[left]=standard
    quicksort(lst,start,left-1)
    quicksort(lst,left+1,end)
