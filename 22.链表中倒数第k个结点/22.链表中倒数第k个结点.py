class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k <1:
            return None
        p = head
        q = head      
        step = 1
        while p.next is not None:
            if step >= k and q is not None:   # 这第二个指针，太妙了！ 在第一个指针已经走了k步后再去走，
                q = q.next
            p = p.next
            step += 1

        if k <= step:
            return q.val
        else:
            return -1


"""
class Solution:
    def FindKthToTail(self , pHead , k ):
        # write code here
        if pHead == None  or k<1:
            return None
        p = pHead
        q = pHead
        step = 1
        while p.next is not None:
            if step >= k and q is not None:
                q = q.next
            p = p.next
            step += 1
        if k <= step:
            return q
        else:
            return None
"""
