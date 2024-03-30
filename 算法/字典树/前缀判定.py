"""
作者：legionb
日期：2024年03月13日
"""
# 重要的是字典树的类要自己会编写
class TrieNode:
    def __init__(self):
        self.children={}
        self.is_red=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i]=TrieNode()
            node = node.children[i]
        node .is_red=True
    def search(self,word):
        node=self.root
        for i in word:
            if i not in node.children:
                return False
            node=node.children[i]
        return True
N,M=map(int,input().split())
T=Trie()
for i in range(N):
    T.insert(input())
for i in range(M):
    if T.search(input()):
        print('Y')
    else:
        print('N')