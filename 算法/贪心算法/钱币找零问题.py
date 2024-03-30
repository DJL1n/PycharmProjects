"""
作者：legionb
日期：2024年03月13日
"""
def slove(money,Count,Value,N):
    num=0
    for i in range(N-1,-1,-1):
        c=min(money//Value[i],Count[i])
        money-=c*Value[i]
        num+=c
    if money>0:
        return -1
    return num



N=7
Count=[3,0,2,1,0,3,5]
Value=[1,2,5,10,20,50,100]
money=int(input())
num=slove(money)
if num==-1:
    print("no")
else:
    print(num)

