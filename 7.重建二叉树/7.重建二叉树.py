# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0:
            return None
        root = TreeNode(pre[0])
        index = tin.index(root.val)
        leftNum = index   # 左边节点的数量，其实这里是 index - 0
        rightNum = len(tin) - leftNum - 1   #  -1 是去除中序遍历的 根节点
        root.left = self.reConstructBinaryTree(pre[1:1+leftNum],tin[0:leftNum])   # 根节点的左子树的，前序遍历 中序遍历  直接递归调用
        root.right = self.reConstructBinaryTree(pre[1+leftNum:],tin[leftNum+1:])  # 根节点的右子树的，前序遍历 中序遍历
        return root