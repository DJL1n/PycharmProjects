"""
作者：legionb
日期：2024年03月14日
"""
#就是把单位重量下价值最高的物品排序然后放进去，01背包需要把一类全部取进去

def asign(W,V,cap,choice):
    perValue=[]
    now=0
    for i in range(len(W)):
        perValue.append(V[i]/W[i])
    sorted_pairs=sorted(zip(perValue,W,V),reverse=True)
    perValue,W,V=zip(*sorted_pairs)
    for i in range(len(W)):
        if now+W[i]<=cap:
            choice[i]=W[i]
            now+=W[i]
        else:
            choice[i]=cap-now
            return choice



n=4 #物品种类
cap=int(input())
W=[10,30,20,5]
V=[200,400,100,10]
choice=[0]*n
print(asign(W, V, cap, choice))
