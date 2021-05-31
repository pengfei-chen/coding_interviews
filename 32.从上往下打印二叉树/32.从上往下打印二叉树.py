
"""
deque是双端队列，双端队列的append（）和pop（）的时间复杂度为O（1），
而list的insert（0，value），append以及pop（）的时间复杂度为O（n）。
"""

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        from Queue import deque
        ans = []
        queue = deque()  # 使用deque而不是list,因为 deque效率更高
        if root is None:
            return ans
        queue.append(root)
        while(len(queue)!=0):
            x = queue.popleft()
            ans.append(x.val)
            if x.left is not None:
                queue.append(x.left)
            if x.right is not None:
                queue.append(x.right)
        return ans