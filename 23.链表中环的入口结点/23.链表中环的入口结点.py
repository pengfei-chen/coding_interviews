# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
链接：https://www.nowcoder.com/questionTerminal/253d2c59ec3e4bc68da16833f79a38e4?f=discussion
来源：牛客网

设置快慢指针，都从链表头出发，快指针每次走两步，慢指针一次走一步，
假如有环，一定相遇于环中某点(结论1)。
接着让两个指针分别从相遇点和链表头出发，两者都改为每次走一步，最终相遇于环入口(结论2)。
"""
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        slow = pHead
        fast = pHead
        while(fast is not None and fast.next is not None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:   # 相遇于环中某点
                fast = pHead
                while(fast!=slow):   # 让两个指针分别从相遇点和链表头出发，两者都改为每次走一步，最终相遇于环入口
                    fast = fast.next
                    slow = slow.next
                return slow
        return None