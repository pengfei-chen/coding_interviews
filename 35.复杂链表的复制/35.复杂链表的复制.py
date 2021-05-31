# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead is None:
            return None
        hashset = dict()
        p = pHead
        helpHead = RandomListNode(-1)
        q = helpHead
        while(p is not None):
            newNode = RandomListNode(p.label)
            hashset[p] = newNode  #字典里面key存的是p这个点
            q.next = newNode
            q = q.next
            p = p.next
            # 复制原来的链表
        p = pHead
        q = helpHead.next
        while(p is not None):
            q.random = hashset.get(p.random,None)   #这里要注意用法！之前不知道能这么用。
            #按照节点数量去对应 p 和 q 对应上
            #这里可以根据p的 random 这个属性，获取对应的key的属性值！
            p = p.next
            q = q.next
        return helpHead.next