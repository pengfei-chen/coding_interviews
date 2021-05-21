# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None and  pHead2 == None:
            return None
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        p = pHead2.next
        q = pHead1
        front = pHead2
        if pHead1.val < pHead2.val:
            front = pHead1
            p = pHead1.next
            q = pHead2
        head = front
        while(p!=None and q!=None):   # p代表第一个元素值最小的那一行
            if q.val < p.val:
                tmp = q.next
                q.next = p      # 这里有点不好理解,因为我们是以p为基准的。
                front.next = q 
                front = q
                q = tmp
            else:
                front = front.next
                p = p.next
        if(q!=None):
            front.next = q   # p 已经排序完了，还余下一部分q
            
        return head