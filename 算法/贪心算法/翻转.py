"""
作者：legionb
日期：2024年04月09日
"""
D=int(input())
for i in range(D):
    target=list(input())
    str1=list(input())
    count=0
    length=len(target)
    for j in range(1,length-1):
        if str1[j]!=str1[j-1] and str1[j]!=str1[j+1] and str1[j]!=target[j]:
            str1[j]='1' if str1[j]=='0' else '0'
            count+=1
    print(count if str1==target else -1)