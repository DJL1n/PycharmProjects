"""
作者：legionb
日期：2024年03月06日
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

left=TreeNode(1)
right=TreeNode(4)
right.left=TreeNode(2)
root=TreeNode(3,left,right)
#right=root.right
#right.left=2


def mid(root):
    if not root:
        return [None]
    return mid(root.left)+[root.val]+mid(root.right)
root=mid(root)
print(root)
