# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        self.q = [pRoot]
        ans = []
        row = 1
        while(len(self.q)!=0):   # q 这个点不为空
            size = len(self.q)
            l = []
            for i in range(0,size):  # 遍历当前q里面的每个点的值
                front = self.q.pop(0)   # 每一次取出 q 前面最开始的元素
                l.append(front.val)
                if front.left is not None:
                    self.q.append(front.left)   #遍历其左子节点，将其左子节点填充进入q点
                if front.right is not None:
                    self.q.append(front.right)  #遍历其右子节点，将其右子节点填充进入q点
            if row&1 == 1:
                ans.append(l[:])   # 奇数行，顺序填充
            else:
                ans.append(l[::-1])  # 偶数行，逆序填充
            row += 1
        return ans