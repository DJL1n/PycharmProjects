"""
作者：legionb
日期：2024年04月14日
"""
n=20000
A=0
B=1
count=0
for i in range(1,n+1):
    A+=i
    B*=i
    if (A-B)%100==0:
        count+=1
        # print(i)
# print(A,B)
print(count)