"""
作者：legionb
日期：2024年04月03日
"""
from collections import defaultdict
res=0
def check_values_equal(dic:defaultdict):
    if not dic:
        return True
    first_value=next(iter(dic))
    return all(value==first_value for value in dic.values())
def juage_balance(tree):
    if not tree:
        return
    juage_balance(tree.left)
    juage_balance(tree.right)
    tree.addColor()
    if check_values_equal(tree.color):
        global res
        res+=1


class Tree:
    def __init__(self,value,left=None,right=None):
        self.color=defaultdict(int)
        self.value=value
        self.left=left
        self.right=right
    def setChild(self,treenode):
        if self.left is None:
            self.left=treenode
        elif self.right is None:
            self.right=treenode
    def setColor(self,color):
        self.color[color]+=1
    def addColor(self):
        if self.left:
            dict1=self.left.color
            for key in dict1:
                self.color[key]+=dict1[key]
        if self.right:
            dict1=self.right.color
            for key in dict1:
                self.color[key]+=dict1[key]



n=int(input())
trees=[]
dads=[]
for i in range(n):
    color,dad=map(int,input().split())
    trees.append(Tree(i))
    trees[i].setColor(color)
    dads.append(dad)
for i in range(1,n):
    trees[dads[i]].setChild(trees[i])
juage_balance(trees[0])
print(res)

