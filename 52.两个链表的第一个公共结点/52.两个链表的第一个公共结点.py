# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 is None or pHead2 is None:
            return None
        count1 = 0
        count2 = 0
        p = pHead1
        while(p is not None):
            p = p.next
            count1 += 1
        p = pHead2
        while(p is not None):
            p = p.next
            count2 += 1
        if count1 > count2:
            p = pHead1
            q = pHead2
        else:
            p = pHead2
            q = pHead1
        count = abs(count1 - count2)
        while(count > 0):
            p = p.next
            count -= 1
        while(p!=q):
                p = p.next
                q = q.next
        return p
        

# 方法二
# 找出2个链表的长度，然后让长的先走两个链表的长度差，然后再一起走
# （因为2个链表用公共的尾部）
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        len1 = self.findListLength(pHead1)
        len2 = self.findListLength(pHead2)
        if len1 > len2:
            pHead1 = self.walkStep(pHead1, len1-len2)
        else:
            pHead2 = self.walkStep(pHead2, len2-len1)
        while(pHead1 != None):
            if pHead1 == pHead2:
                return pHead1
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return pHead1
        
    def findListLength(self, pHead1):
        if pHead1 == None:
            return 0
        sum = 1
        while(pHead1.next != None):
            sum += 1
            pHead1 = pHead1.next
        return sum
    
    def walkStep(self,pHead1, step):
        while(step>0):
            pHead1 = pHead1.next
            step -= 1
        return pHead1