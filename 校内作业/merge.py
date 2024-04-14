"""
作者：legionb
日期：2024年04月14日
"""
def merge(list1,list2):
    i,j=0,0
    res=[]
    while i<len(list1) and j<len(list2):
        if list1[i]>list2[j]:
            res.append(list1[i])
            i+=1
        elif list2[j]>list1[i]:
            res.append(list2[j])
            j+=1
    while i<len(list1):
        res.append(list1[i])
        i+=1
    while j<len(list2):
        res.append(list2[j])
        j+=1
    return res
mylist1 = [44, 32, 31, 21, 11, 6, 5]
mylist2 = [34, 22, 17, 15, 13, 4, 2]
my_orderedlist = merge(mylist1, mylist2)
print(my_orderedlist)