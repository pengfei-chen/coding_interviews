# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        stack = []
        cur = pRootOfTree
        prev = None
        head = None
        while(True):
            while(cur is not None):
                stack.append(cur)
                cur = cur.left   # 一直到当前节点能到的，最左子节点
            if len(stack) == 0:
                break
            cur = stack.pop()   # 只要stack 不为空，就会往下走
            if prev is None:   # 当前斜列的最左下脚节点
                cur.left = None  
                head = cur
            else:
                prev.right = cur  # 上一个斜列的点，由none，转变成cur，有何意义？
                cur.left = prev
            prev = cur
            cur = cur.right
        return head


"""
先中序遍历，将所有的节点保存到一个列表中。
对这个list[:-1]进行遍历，每个节点的right设为下一个节点，下一个节点的left设为上一个节点。
"""
# 太厉害了！
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:return 
        self.arr = []
        self.midTraversal(pRootOfTree)
        for i,v in enumerate(self.arr[:-1]):
            v.right = self.arr[i + 1]
            self.arr[i + 1].left = v
        return self.arr[0]

    def midTraversal(self, root):   # 递归中序遍历
        if not root: return
        self.midTraversal(root.left)
        self.arr.append(root)
        self.midTraversal(root.right)

