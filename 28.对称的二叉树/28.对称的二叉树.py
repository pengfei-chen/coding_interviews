
# 思路：首先根节点以及其左右子树，左子树的左子树和右子树的右子树相同
# 左子树的右子树和右子树的左子树相同即可，采用递归
# 非递归也可，采用栈或队列存取各级子树根节点


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return self.comRoot(pRoot.left, pRoot.right)
    
    def comRoot(self,left,right):
        if left == None and right == None:
            return True
        if left == None and right != None:
            return False
        if right == None:
            return False
        if left.val != right.val:
            return False
        return self.comRoot(left.left, right.right) and self.comRoot(left.right, right.left)