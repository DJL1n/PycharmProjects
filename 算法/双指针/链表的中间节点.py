"""
作者：legionb
日期：2024年04月06日
"""


# 快慢指针
# 当快指针到结尾时，慢指针的位置就是中间节点
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
